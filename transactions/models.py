from django.db import models


class Transaction(models.Model):
    type = models.CharField(max_length=1)
    date = models.CharField(max_length=8)
    value = models.IntegerField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    # Hora da ocorrência atendendo ao fuso de UTC-3
    hour = models.CharField(max_length=6)
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
