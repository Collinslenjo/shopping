from .models import Shoppinglist,ShoppinglistItem
from rest_framework import serializers


class ShoppinglistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shoppinglist
		fields = ("listName", "budgetAmount","user","budgetLimit")

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = ShoppinglistItem
		fields = ("itemName", "quantity", "price","shoppinglist","bought")