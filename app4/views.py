from django.http.response import HttpResponse

from .serializer import SerializerApp4notes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import App4Notes

# Create your views here.
@api_view(['GET'])
def App4views(request):
    getobjects = App4Notes.objects.all()
    serializer = SerializerApp4notes(getobjects, many=True)
    return Response(serializer.data)