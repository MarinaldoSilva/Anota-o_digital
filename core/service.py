from .models import Anotacao
from .serializer import AnotacaoSerializer

class AnotacaoService:

    @staticmethod
    def get_all_anotacao():
        anotacao = Anotacao.objects.all()
        serializer = AnotacaoSerializer(anotacao, many=True)
        return serializer.data, None
    
    @staticmethod
    def create_anotacao(data):
        serializer = AnotacaoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
    
    @staticmethod
    def get_pk_anotacao(pk):
        try:
           anotacao = Anotacao.objects.get(pk=pk)
        except Anotacao.DoesNotExist:
            return None,{"Errors": "ID não localizado"}
        
        serializer = AnotacaoSerializer(anotacao)
        return serializer.data, None
    
    @staticmethod
    def update_anotacao(pk, data, partial=False):
        try:
           anotacao = Anotacao.objects.get(pk=pk)
        except Anotacao.DoesNotExist:
            return None,{"Errors": "ID não localizado"}
        
        serializer = AnotacaoSerializer(instance=anotacao, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
    
    @staticmethod 
    def delete_anotacao(pk):
        try:
           anotacao = Anotacao.objects.get(pk=pk)
           anotacao.delete()
           return True, None
        except Anotacao.DoesNotExist:
            return False,{"Errors": "ID não localizado"}
        
