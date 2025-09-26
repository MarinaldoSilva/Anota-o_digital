from rest_framework import serializers
from .models import Anotacao

class AnotacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anotacao
        fields = ['id','titulo','descricao','data_criacao']
        read_only_fields = ['id','data_criacao']
