from.models import *
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=50)
    size_or_weight = serializers.CharField(max_length=10)

    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    
    def update(self, product, validated_data):
            product.name = validated_data.get('name', product.name)
            product.category = validated_data.get('category', product.category)
            product.size_or_weight = validated_data.get('size_or_weight', product.size_or_weight)
            product.save()
            return product
    

class CartSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=50)
    product = serializers.CharField(max_length=50)
    quantity = serializers.IntegerField()

    
    def create(self, validated_data):
        return Cart.objects.create(**validated_data)

    def update(self, cart, validated_data):
        newCart = Cart(**validated_data)
        newCart.id = cart.id
        newCart.save()
        return newCart


