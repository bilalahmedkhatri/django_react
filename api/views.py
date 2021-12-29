from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Note
from .serializers.noteserializer import NoteSerializer

# Create your views here.

@api_view(['GET'])
def testApi(request):
    testapi = [
        {
            'id':  1,
            "name": "muhammad Aashaaz",
            "age": 3,
            "father_name": "Bilal Ahmed",
        }
    ]
    return Response(testapi)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)