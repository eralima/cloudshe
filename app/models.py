from django.db import models

# Create your models here.

class Company(models.Model):
    nome = models.CharField(max_length=150)
    razao_social = models.CharField(max_length=150)
    email = models.EmailField()
    rua = models.CharField(max_length=150)
    cep = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    telefone = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=150)

class Produtos(models.Model):
    imagem_link = models.CharField(max_length=500)
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.IntegerField()
    marca = models.CharField(max_length=150)
    empresa = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='produtos')
















