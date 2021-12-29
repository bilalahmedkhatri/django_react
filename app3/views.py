from rest_framework.decorators import api_view
from .models import App3Model
from .serializer_test import App3Serializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def App3Notes(request):
    get_ = App3Model.objects.all()
    serializer = App3Serializer(get_, many=True)
    return Response(serializer.data)