from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.decorators import api_view

# Función para obtener nuestros productos
@api_view(['GET'])
def obtener(request):
    producto = Producto.objects.all()
    serializer = ProductoSerializer(producto, many = True)
    return Response(serializer.data)

# Función para crear un nuevo producto
@api_view(['POST'])
def crear(request):
    serializer = ProductoSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({"message":"Ops hay algo mal en la petición"})

# Función para actualizar un producto existente
@api_view(['PUT'])
def actualizar(request, pk):
    data = Producto.objects.get(id=pk)
    serializer = ProductoSerializer(data=request.data, instance=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({"message":"Ops hay algo mal en la petición"})

# Función para eliminar un producto
@api_view(['DELETE'])
def eliminar(request, pk):
    data = Producto.objects.get(id=pk)
    data.delete()
    return Response ({"message": "Se eliminó correctamente"})