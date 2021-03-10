from rest_framework import filters
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from main.models import Product
from main.serializers import ProductListSerializer


class HomePageView(APIView):

    def get(self, request):
        return Response("Hello world", status=status.HTTP_200_OK)


class SearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title', '=owner']