from .models import Product
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
