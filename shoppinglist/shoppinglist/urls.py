from rest_framework.urlpatterns import format_suffix_patterns
from .views import listAllShoppingListsView, listShoppinglistItemsView
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include
from django.urls import path


urlpatterns = [
    path(r'lists/', listAllShoppingListsView.as_view(), name="allShoppingLists"),
    url(r'lists/(?P<pk>\d+)/$', listAllShoppingListsView.as_view()),
    path('items/', listShoppinglistItemsView.as_view(), name="items"),
    url(r'items/(?P<pk>\d+)/$', listShoppinglistItemsView.as_view()),
    url(r'^get-token/', obtain_auth_token)
]
# urlpatterns = format_suffix_patterns(urlpatterns)