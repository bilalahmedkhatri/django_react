from rest_framework.serializers import ModelSerializer
from .models import App6Model

class App6Serializer(ModelSerializer):
    class Meta:
        model = App6Model
        fields = ('id', 'name', 'description')