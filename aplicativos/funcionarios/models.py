from django.contrib.auth.models import User
from django.db import models

from aplicativos.departamentos.models import Departamentos
from aplicativos.empresas.models import Empresas


# Create your models here.
class Funcionarios(models.Model): 
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamentos)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    