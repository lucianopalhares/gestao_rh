from django.db import models


# Create your models here.
class Empresas(models.Model):
    name = models.CharField(max_length=100, help_text='Nome da Empresa')

    def __str__(self):
        return self.name
    