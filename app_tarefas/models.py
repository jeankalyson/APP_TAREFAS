from django.db import models

class Tarefa(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    nome_tarefa = models.TextField(max_length= 100,null=False, blank=False)
    data = models.DateField()
    hora = models.TimeField()


