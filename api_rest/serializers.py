from rest_framework.serializers import ModelSerializer
from .models import Producto

class ProductoSerializer(ModelSerializer):
    class Meta:
        model= Producto
        fields= '__all__'