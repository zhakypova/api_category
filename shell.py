# import json
# import io
# from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
#
# class Category:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
#
#
# categories = Category(name='Sportswear', code='12345678')
#
# class CategorySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=20)
#     code = serializers.CharField(max_length=8)
#
# serializer = CategorySerializer(categories)
# # print(serializer.data)
#
# jsoncategory = JSONRenderer().render(serializer.data)
# print(jsoncategory)
#
#
# class Item:
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category
#
# items = Item(name='sneakers', price=200)
#
#
