from rest_framework import filters
from rest_framework import generics

from main.models import Product
from main.serializers import ProductListSerializer


class SearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title', '=owner']