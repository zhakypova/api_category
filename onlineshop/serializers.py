from rest_framework import serializers
import io
from rest_framework.parsers import JSONParser
from .models import Category, Item




class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.save()
        return instance

    def validate_name(self, value):
        sim_list = ['!','@','#','$','%','^','&','*']
        for i in sim_list:
            if i in value:
                raise serializers.ValidationError('Название категорий не может содержать специальных символов ('
                                                  '!@#$%^&*)')
        return value

class ItemSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()
    QR = serializers.ReadOnlyField(source='get_QR')


    class Meta:
        validators = [
            serializers.UniqueTogetherValidator(
                Item.objects.all(),
                fields=['item_id',]
            )
        ]


    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.item_id = validated_data['item_id']
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        instance.category_id = validated_data['category_id']
        instance.QR = validated_data['QR']
        instance.save()
        return instance



    # def save(self, **kwargs):
    #     print(f'{self.category_id}C{self.price}P{self.item_id}l')
    #     super().save(**kwargs)
