from django.db import models

class Docente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Horario(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    disciplina = models.CharField(max_length=100)
    ano = models.IntegerField()
    dia = models.CharField(max_length=20)
    inicio = models.TimeField()
    fim = models.TimeField()

    def __str__(self):
        return f"{self.disciplina} - {self.docente.nome}"
