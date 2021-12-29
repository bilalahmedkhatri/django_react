from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import App6Serializer

# from backend.app6.serializer import App6Serializer
from .models import App6Model
# Create your views here.


@api_view(['GET'])
def App6Notes(request):
    get_x = App6Model.objects.all()
    serializers = App6Serializer(get_x, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def App6Note(request,pk):
    get_x = App6Model.objects.get(id=pk)
    serializers = App6Serializer(get_x, many=False)
    return Response(serializers.data)