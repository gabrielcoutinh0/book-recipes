from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Receita(models.Model):
  pessoa = models.ForeignKey(User, on_delete = models.CASCADE)
  nome = models.CharField(max_length = 200)
  ingredientes = models.TextField()
  modo_preparo = models.TextField()
  tempo_preparo = models.IntegerField()
  rendimento = models.IntegerField()
  categoria = models.CharField(max_length = 100)
  data_receita = models.DateTimeField(default = datetime.now, blank = True)
  foto = models.ImageField(upload_to = 'fotos/%d/%m/%Y', blank = True)
  publicado = models.BooleanField(default = False)

  def __str__(self):
    return self.nome