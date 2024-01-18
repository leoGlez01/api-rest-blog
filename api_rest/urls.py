from django.urls import path
from .views import *

urlpatterns = [
    path('api/', obtener, name='obtener'),
    path('api/post/', crear, name='crear'),
    path('api/put/<int:pk>/', actualizar, name='actualizar'),
    path('api/delete/<int:pk>/', eliminar, name='eliminar')
]