from django.db import models

class Member(models.Model):
	nome=models.CharField(max_length=100)
	sobrenome=models.CharField(max_length=100)
	curso=models.CharField(max_length=100)
