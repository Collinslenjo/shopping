from .serializers import ShoppinglistSerializer,ItemSerializer
from .models import Shoppinglist,ShoppinglistItem
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import status
from django.shortcuts import render
from .permissions import IsOwner

# Create your views here.
# ShoppingList View
class listAllShoppingListsView(generics.ListAPIView):
	queryset = Shoppinglist.objects.all()
	serializer_class = ShoppinglistSerializer
	permission_classes = (
		permissions.IsAuthenticated, IsOwner)

	def post(self,request, **kwargs):
		List = Shoppinglist.objects.create(
			listName=request.data["listName"],
			user = User.objects.get(id=request.data["user"]),
			budgetAmount = request.data["budgetAmount"])
		return Response(
			data= ShoppinglistSerializer(List).data,
			status=status.HTTP_201_CREATED
			)


	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

# ShoppingList Items View
class listShoppinglistItemsView(generics.ListAPIView):
	queryset = ShoppinglistItem.objects.all()
	serializer_class = ItemSerializer
	permission_classes = (
		permissions.IsAuthenticated, IsOwner)

	def post(self,request, **kwargs):
		Item = ShoppinglistItem.objects.create(
			itemName=request.data["itemName"],
			shoppinglist = Shoppinglist.objects.get(id=request.data["shoppinglist"]),
			quantity = request.data["quantity"],
			price = request.data["price"])
		return Response(
			data= ItemSerializer(Item).data,
			status=status.HTTP_201_CREATED
			)