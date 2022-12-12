from rest_framework import serializers

from .models import Category, Item

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    code = serializers.CharField(max_length=8)


    def create(self, validated_data):
        return Category.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.code = validated_data['code']
        instance.save()
        return instance


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        instance.save()
        return instance
