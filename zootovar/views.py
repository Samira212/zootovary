from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import Cat, CatFilter


class CatViewSets(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = CatFilter
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = CatFilter
    permission_classes = [permissions.IsAuthenticated]

