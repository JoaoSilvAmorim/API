from myapp.serializer import MicrodadosSerializer
from .models import MICRODADOS
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

class Casos(APIView):
    def get_object(self, id):
        try:
            return MICRODADOS.objects.filter(id=id).get()
        except Casos.DoesNotExist:
            raise Http404
        
    def get(self, request, id = None, format=None):
        if id:
            serializer = MicrodadosSerializer(self.get_object(id))
            return Response(serializer.data)
        else:
            casos = MICRODADOS.objects.all()
            serializer = MicrodadosSerializer(casos, many=True)
            return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MicrodadosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        caso = self.get_object(id)
        caso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, id, format=None):
        caso = self.get_object(id)
        serializer = MicrodadosSerializer(data = request.data)
        serializer.update(caso, request.data)
        return Response(status=status.HTTP_200_OK)
    
