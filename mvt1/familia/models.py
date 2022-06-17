from django.db import models


class Familiar(models.Model):

    nombre = models.CharField('NOMBRE',max_length=30)
    apellido = models.CharField('APELLIDO',max_length=30)
    nacimiento = models.DateField('FECHA DE NACIMIENTO')

    class Meta:
        verbose_name_plural = 'Familiares'





