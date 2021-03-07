from rest_framework import serializers
from .models import Product, Review


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'owner',
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


class ReviewsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            'title',
            'review',
            'author'
        ]


class ReviewsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            'title',
            'review',
        ]