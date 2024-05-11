from django.db import models

from aplicativos.funcionarios.models import Funcionarios


# Create your models here.
class RegistroHoraExtra(models.Model):
    name = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    