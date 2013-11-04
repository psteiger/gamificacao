from django.db import models

class Funcao(models.Model):
	nome = models.CharField(max_length=100)

class Funcionario(models.Model):
	nome = models.CharField(max_length=100)
	funcao = models.ForeignKey(Funcao)
	equipe = models.ForeignKey(Equipe)
	foto = models.ImageField(upload_to='/tmp')

class Equipe(models.Model):
	nome = models.CharField(max_length=100)
	responsavel = models.ForeignKey(Funcionario)

class Regra(models.Model):
	peso = models.IntegerField()
	nome = models.CharField(max_length=100)
	