from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .service import AnotacaoService


class AnotacaoListCreateAPIVIew(APIView):
    def get(self, request):
        anotacao, error = AnotacaoService.get_all_anotacao()
        if error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        return Response(anotacao, status=status.HTTP_200_OK)
    
    def post(self, request):
        anotacao, error = AnotacaoService.create_anotacao(request.data)
        if error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        return Response(anotacao, status=status.HTTP_201_CREATED)

class AnotacaoDetailAPIView(APIView):
    def get(self, request, pk):
        anotacao, error = AnotacaoService.get_pk_anotacao(pk)
        if error:
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        return Response(anotacao, status=status.HTTP_200_OK) 
    
    def patch(self, request, pk):
        anotacao, error = AnotacaoService.update_anotacao(pk, request.data, partial=True)
        if error:
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        return Response(anotacao, status=status.HTTP_200_OK) 

    def put(self, request, pk):
        anotacao, error = AnotacaoService.update_anotacao(pk, request.data)
        if error:
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        return Response(anotacao, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        anotacao, error = AnotacaoService.delete_anotacao(pk)
        if error:
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT) 