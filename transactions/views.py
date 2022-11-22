from django.shortcuts import render
from .models import Transaction
from rest_framework.views import APIView, status
from rest_framework.response import Response

from django.forms import model_to_dict


class TransactionView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()

        transactions_dict = [model_to_dict(transaction) for transaction in transactions]

        soma = 0
        for transaction in transactions_dict:
            # Debito tira, tal e tal adiciona...
            soma += transaction["value"]

        print(soma)
        transactions_dict.append({"total_value": soma})
        return Response(transactions_dict, status.HTTP_200_OK)


def form(request):

    # if request.method == "POST":
    # Talvez try except aqui
    # uploadedFile = request.FILES["uploadedFile"]

    # destination = open("transactions.txt", "wb+")
    # for chunk in uploadedFile.chunks():
    #     # print(uploadedFile.read())
    #     destination.write(chunk)
    # destination.close()

    # documents = models.Document.objects.all()
    if request.method == "POST":

        uploadedFile = request.FILES["uploadedFile"]

        destination = open("transactions.txt", "wb+")
        for chunk in uploadedFile.chunks():
            # print(uploadedFile.read())
            destination.write(chunk)
        destination.close()

        # Transformar função

        file = open("transactions.txt", encoding="utf-8")

        transactions = file.readlines()

        for transaction in transactions:
            transactionDict = read_transaction(transaction)
            Transaction.objects.create(**transactionDict)
            print(transactionDict)

    return render(request, "form/index.html")


def read_transaction(transaction: str):
    # file = open("transactions.txt")

    # transactions = file.readlines()
    # value = transaction[9:19] / 100
    print(int(transaction[9:19]))
    # for transcaction in transactions:
    transactionDict = {
        "type": transaction[0:1],
        "date": f"{transaction[7:9]}/{transaction[5:7]}/{transaction[1:5]}",
        "value": int(transaction[9:19]) / 100,
        "cpf": f"{transaction[19:22]}.{transaction[22:25]}.{transaction[25:28]}-{transaction[28:30]}",
        "card": transaction[30:42],
        "hour": f"{transaction[42:44]}:{transaction[44:46]}:{transaction[46:48]}",
        "store_owner": transaction[48:62],
        "store_name": transaction[62:81],
    }

    return transactionDict


# class TransictionView(APIView):
#     def post(self, request):

#         # Transformar função
#         uploadedFile = request.FILES["uploadedFile"]

#         destination = open("transactions.txt", "wb+")
#         for chunk in uploadedFile.chunks():
#             # print(uploadedFile.read())
#             destination.write(chunk)
#         destination.close()

#         # Transformar função

#         file = open("transactions.txt")

#         transactions = file.readlines()

#         for transaction in transactions:
#             transactionDict = read_transaction(transaction)
#             Transaction.objects.create(transactionDict)
