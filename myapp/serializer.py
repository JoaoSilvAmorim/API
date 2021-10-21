from copy import error
from django.db.models import fields
from rest_framework import serializers
from rest_framework.response import Response
from .models import MICRODADOS



class MicrodadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MICRODADOS
        
        fields = (
            "id",
            "MUNICIPIO",
            "REGIAO", 
            "NATUREZA", 
            "DATA", 
            "ANO", 
            "SEXO",
            "IDADE",
            "ENVOLVIDOS",
        )
        
    def create(self, validated_data):
        MICRODADOS.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        for chave, valor in validated_data.items():
            setattr(instance, chave, valor)
            instance.save()