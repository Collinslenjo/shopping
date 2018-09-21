from django.test import TestCase
from django.urls import reverse
from .models import Shoppinglist
from rest_framework.views import status
from django.contrib.auth.models import User
from .serializers import ShoppinglistSerializer
from rest_framework.test import APITestCase, APIClient

# Create your tests here.
class BaseViewTest(APITestCase):

	@staticmethod
	def create_list(listName="",user="",budgetAmount=""):
		if listName != "" and user !="" and budgetAmount !="":
			Shoppinglist.objects.create(listName=listName,user=user,budgetAmount=budgetAmount)

	def setUp(self):
		# set test data
		my_user = User.objects.get_or_create(username="test_user")
		user = my_user[0]
		client = APIClient()
		self.client.force_authenticate(user=user)
		self.create_list("Food Shopping",user,20000)
		# self.create_list("Car Accessories",user,5000)
		# self.create_list("Home Appliances",user,4500)
		self.shoppinglist_data = {'listName': 'Picnic', 'user': user,'budgetAmount': 600}

class getShoppingListsTest(BaseViewTest):

	def test_get_shoppinglists(self):
		response = self.client.get(reverse("allShoppingLists", kwargs={"version": "v1"}))
		expected = Shoppinglist.objects.all()
		serialized = ShoppinglistSerializer(expected, many=True)
		self.assertEqual(response.data, serialized.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_can_add_list(self):
		response = self.client.post("/api/v1/lists/",self.shoppinglist_data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	# def test_list_can_update(self):
	# 	shoppinglist = Shoppinglist.objects.get()
	# 	change_shoppinglist = {'listName': 'New List'}
	# 	res = self.client.put("/api/v1/lists/"+str(shoppinglist.id)+"/",change_shoppinglist, format='json')
	# 	print("/api/v1/lists/"+str(shoppinglist.id))
	# 	self.assertEqual(res.status_code, status.HTTP_200_OK)

	def test_authorization_is_working(self):
		new_client = APIClient()
		res = new_client.get(reverse("items", kwargs={"version": "v1"}))
		self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)