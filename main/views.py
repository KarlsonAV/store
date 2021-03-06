from rest_framework.views import APIView
from django.core import serializers
from .serializers import ProductListSerializer, ProductDetailSerializer
from users.models import User
from .models import Product
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, authentication, permissions


class ProductListView(APIView):

    def get(self, request, format=None):
        all_products = [ProductListSerializer(instance=product).data for product in Product.objects.all()]
        context = {
            'all_products': all_products
        }
        return Response(context, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk, format=None):
        check = Product.objects.get(pk=pk)
        product = ProductDetailSerializer(Product.objects.get(pk=pk)).data
        context = {
            'product': product
        }
        return Response(context, status=status.HTTP_200_OK)