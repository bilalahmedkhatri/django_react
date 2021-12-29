from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import App2
from .serializer.appserializer import appNotesSerializer
# Create your views here.

@api_view(['GET'])
def app2Notes(request):
    appnotes = App2.objects.all()
    resultSerializer = appNotesSerializer(appnotes)
    return Response(resultSerializer.data)



