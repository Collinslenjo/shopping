from .serializers import ShoppinglistSerializer,ItemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Shoppinglist,ShoppinglistItem
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import status
from django.shortcuts import render
from .permissions import IsOwner

# Create your views here.
# ShoppingList View
class listAllShoppingListsView(generics.ListCreateAPIView):
	queryset = Shoppinglist.objects.all()
	serializer_class = ShoppinglistSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('listName')
	permission_classes = (
		permissions.IsAuthenticated, IsOwner)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class listAllShoppingListsDetailsView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	queryset = Shoppinglist.objects.all()
	serializer_class = ShoppinglistSerializer
	permission_classes = (
		permissions.IsAuthenticated, IsOwner)

	def get(self,request,pk=None, **kwargs):
		shoppinglist = Shoppinglist.objects.get(id=pk)
		items = ShoppinglistItem.objects.get(shoppinglist_id=shoppinglist.id)
		return Response(
			data= ItemSerializer(items).data,
			status=status.HTTP_200_OK)

	def post(self,request, **kwargs):
		List = Shoppinglist.objects.create(
			listName=request.data["listName"],
			user = User.objects.get(id=request.data["user"]),
			budgetAmount = request.data["budgetAmount"],
			budgetLimit = request.data["budgetLimit"])
		return Response(
			data= ShoppinglistSerializer(List).data,
			status=status.HTTP_201_CREATED
			)

	def update(self, request, pk=None,**kwargs):
		newlist = Shoppinglist.objects.get(id=pk)
		newlist.listName=request.data["listName"]
		newlist.user = User.objects.get(id=request.data["user"])
		newlist.budgetAmount = request.data["budgetAmount"]
		newlist.budgetLimit = request.data["budgetLimit"]
		newlist.save()
		return Response(
			data= ShoppinglistSerializer(newlist).data,
			status=status.HTTP_200_OK)

# ShoppingList Items View
class listShoppinglistItemsView(generics.ListCreateAPIView):
	queryset = ShoppinglistItem.objects.all()
	serializer_class = ItemSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('itemName', 'price')
	permission_classes = (
		permissions.IsAuthenticated, IsOwner)


class listShoppinglistItemsDetailsView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	queryset = ShoppinglistItem.objects.all()
	serializer_class = ItemSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('itemName', 'price')
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

	def update(self, request, pk=None,**kwargs):
		newitem = ShoppinglistItem.objects.get(id=pk)
		newitem.itemName=request.data["itemName"]
		newitem.shoppinglist = Shoppinglist.objects.get(id=request.data["shoppinglist"])
		newitem.quantity = request.data["quantity"]
		newitem.price = request.data["price"]
		if request.data["bought"] == "" or request.data["bought"] == None:
			pass
		else:
			newitem.bought = request.data["bought"]
		newitem.save()
		return Response(
			data= ItemSerializer(newitem).data,
			status=status.HTTP_200_OK)