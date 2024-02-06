from django.urls import path, include
from .models import Post, Product
from rest_framework import routers, serializers, viewsets


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['name', 'text', 'image']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
