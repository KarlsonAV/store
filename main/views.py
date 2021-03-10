from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from django.db.models import Q
from django.core import serializers
from .serializers import ProductListSerializer, ProductDetailSerializer, ReviewsListSerializer, ReviewsCreateSerializer
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
        queryset = Product.objects.get(pk=pk)
        product = ProductDetailSerializer(queryset).data
        reviews = [ReviewsListSerializer(instance=review).data for review in queryset.reviews.all()]
        context = {
            'product': product,
            'reviews': reviews,
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, pk, format=None):
        data = dict(request.data.items())
        serializer = ReviewsCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user, product=Product.objects.get(pk=pk))
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCreateView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, format=None):
        serializer = ProductDetailSerializer(data=request.data)
        if serializer.is_valid():
            print('VALID')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk, format=None):
        data = Product.objects.get(pk=pk)
        data.delete()
        return Response(status=status.HTTP_200_OK)


class ProductUpdateView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        data = request.data
        product.title = data['title']
        product.description = data['description']
        product.owner = data['owner']
        product.price = data['price']
        product.cover = data['cover']
        product.save()
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FilterByCategory(APIView):

    def get(self, request, format=None):
        tags = request.GET.get('categories')
        if tags:
            object = Product.objects.filter(Q(categories__icontains=tags))
            filtered_products = [ProductListSerializer(instance=product).data for product in object]
            context = {
                'filtered_products': filtered_products,
            }
            return Response(context, status=status.HTTP_200_OK)
        return Response('There is nothing', status=status.HTTP_200_OK)