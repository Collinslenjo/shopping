from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models
# Create your models here.

class Shoppinglist(models.Model):
	listName = models.CharField(max_length=255, null=False)
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='shopping_lists')
	budgetAmount = models.DecimalField(_('budget_amount(KES)'),max_digits=7, decimal_places=2, default=0.00)
	budgetLimit = models.DecimalField(_('budget_balance(KES)'),max_digits=7, decimal_places=2, default=0.00)
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{} - {}".format(self.listName,self.user,self.budgetAmount,self.budgetBalance)

	class Meta:
		db_table = 'tbl_shoppinglists'

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)

class ShoppinglistItem(models.Model):
	itemName = models.CharField(max_length=255, null=False)
	quantity = models.DecimalField(_('quantity'),max_digits=7, decimal_places=2, default=0.00)
	price = models.DecimalField(_('budget_amount(KES)'),max_digits=7, decimal_places=2, default=0.00)
	shoppinglist = models.ForeignKey(Shoppinglist, on_delete=models.CASCADE, related_name='shopping_items')
	bought = models.BooleanField(default=False)
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{} - {}".format(self.itemName,self.quantity,self.price,self.shoppinglist,self.bought)

	class Meta:
		db_table = 'tbl_shoppinglist_items'