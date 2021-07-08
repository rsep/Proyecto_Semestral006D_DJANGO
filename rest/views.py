from django.views.decorators.csrf import csrf_exempt
from rest.serializers import ObraSerializer
from django.shortcuts import render
from core.models import Obra
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
#GET : Listar todos las obras
#POST: Nueva Obra

@csrf_exempt
@api_view(['GET'])

def lista_obra(request):
    if request.method == 'GET':
        obra = Obra.objects.all()
        serializer = ObraSerializer(obra,many=True) 
        return Response(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ObraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
             Response (serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_obra(request, id):
        try:
            obra = Obra.objects.get(id_obra=id)    
        except Obra.DoesNotExist: 
            return Response(status.HTTP_404_NOT_FOUND) 

        if request.method == 'GET':
            serializer = ObraSerializer(obra)
            return Response(serializer.data)

        if request.method =='PUT':
            data = JSONParser().parse(request)
            serializer = ObraSerializer(obra,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
             Response (serializer.error, status=status.HTTP_400_BAD_REQUEST)

             if request.method == 'DELETE':
                 Obra.delete()
                 return Response(status.HTTP_204_NO_CONTENT)


