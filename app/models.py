from django.db import models

# Create your models here.

class Produtos(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.IntegerField()
    marca = models.CharField(max_length=150)


class Company(models.Model):
    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    rua = models.CharField(max_length=150)
    cep = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    fone = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=150)














