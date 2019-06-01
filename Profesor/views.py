# ------------Librerias------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# ----------------Modelos--------------
# Nombre app                      nombre modelo
from Profesor.models import Profesor
# ----------------serializers-------------
from Profesor.serializers import ProfesorSerializers

# ------------------LIBRERIAS EXTERNAS------------------
# import json

class ProfesorList(APIView):
    # METODO PARA EXPLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = Profesor.objects.all()
        #                               ,context = {'request':request}
        serializer = ProfesorSerializers(queryset, many=True, context = {'request':request})
        return Response(serializer.data)
    # METODO PARA CREAR NUEVO REGISTRO 
    def post(self, request, format=None):
        serializer = ProfesorSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response (datas)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
class ProfesorDetail(APIView):
    #METODO PARA COSULTAR ID Y E RETORNE SI EXISTE O NO
    def get_object(self,pk):
        try: 
            return Profesor.objects.get(pk=pk)
        except Profesor.DoesNotExist:
            raise Http404
    #METODO PARA CONSULTAR ID Y DEVOLVER LOS VALORES DE SUS CAMPOS 
    def get(self, request,pk, format=None):
        profesor = self.get_object(pk) 
        serializer = ProfesorSerializers(profesor)
        return Response(serializer.data)
    #METODO CONSULTAR ID Y ACTUALIZAR DATOS 
    def put(self, request,pk, format=None):
        profesor = self.get_object(pk)
        serializer = ProfesorSerializers(profesor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profesor = self.get_object(pk)
        profesor.delete()
        return Response('eliminado')
