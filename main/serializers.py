from rest_framework import serializers
from users.models import User
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
        ]


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'cover',
            'owner',
        ]