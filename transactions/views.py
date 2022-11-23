from django.shortcuts import render, redirect
from .models import Transaction
from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.forms import model_to_dict

from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect


class TransactionView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()

        transactions_dict = [model_to_dict(transaction) for transaction in transactions]

        total_value = 0
        for transaction in transactions_dict:
            if transaction["type"] in "239":
                total_value -= transaction["value"]
            else:
                total_value += transaction["value"]

        transactions_dict.append({"total_value": f"R$ {total_value}"})

        return Response(transactions_dict, status.HTTP_200_OK)


def form(request):

    if request.method == "POST":

        uploadedFile = request.FILES["uploadedFile"]

        destination = open("transactions.txt", "wb+")
        for chunk in uploadedFile.chunks():
            destination.write(chunk)
        destination.close()

        file = open("transactions.txt", encoding="utf-8")
        transactions = file.readlines()
        for transaction in transactions:
            transactionDict = read_transaction(transaction)
            Transaction.objects.create(**transactionDict)
        file.close()

        return redirect("/api/transactions/")

    return render(request, "form/index.html")


def read_transaction(transaction: str):

    transactionDict = {
        "type": transaction[0:1],
        "date": f"{transaction[7:9]}/{transaction[5:7]}/{transaction[1:5]}",
        "value": int(transaction[9:19]) / 100,
        "cpf": f"{transaction[19:22]}.{transaction[22:25]}.{transaction[25:28]}-{transaction[28:30]}",
        "card": transaction[30:42],
        "hour": f"{transaction[42:44]}:{transaction[44:46]}:{transaction[46:48]}",
        "store_owner": transaction[48:62].rstrip(),
        "store_name": transaction[62:81].rstrip("\n").rstrip(" "),
    }

    return transactionDict
