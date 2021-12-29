from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import App5Notes
from .serializer import App5NotesSerializer 
# Create your views here.

@api_view(['GET'])
def app5Notes(request):
    al = App5Notes.objects.all()
    serializer = App5NotesSerializer(al, many=True)
    return Response(serializer.data)