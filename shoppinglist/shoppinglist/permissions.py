from rest_framework.permissions import BasePermission
from .models import Shoppinglist

class IsOwner(BasePermission):
	def has_object_permission(self, request, view, obj):
		if isinstance(obj, Shoppinglist):
			return obj.owner == request.user
		return obj.owner == request.user