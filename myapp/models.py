from django.db import models
import uuid
from django.core.files import File
from django.db import models
from myapi.settings import DATABASES


class MICRODADOS(models.Model):
    MUNICIPIO =  models.CharField(null=True, blank=True, max_length=64)
    REGIAO = models.CharField(null=True, blank=True, max_length=64)
    NATUREZA = models.CharField(null=True, blank=True, max_length=64)
    DATA = models.CharField(null=True, blank=True, max_length=64)
    ANO = models.CharField(null=True, blank=True, max_length=64)
    SEXO = models.CharField(null=True, blank=True, max_length=64)
    IDADE = models.CharField(null=True, blank=True, max_length=64)
    ENVOLVIDOS = models.CharField(null=True, blank=True, max_length=64)
    
    class Meta:
        ordering = ('MUNICIPIO', )