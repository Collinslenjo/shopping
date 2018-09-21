from .views import listAllShoppingListsView, listShoppinglistItemsView,listAllShoppingListsDetailsView,listShoppinglistItemsDetailsView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include
from django.urls import path


urlpatterns = [
    path(r'lists/', listAllShoppingListsView.as_view(), name="allShoppingLists"),
    url(r'lists/(?P<pk>\d+)/$', listAllShoppingListsDetailsView.as_view()),
    path('items/', listShoppinglistItemsView.as_view(), name="items"),
    url(r'items/(?P<pk>\d+)/$', listShoppinglistItemsDetailsView.as_view()),
    url(r'^get-token/', obtain_auth_token)
]
# urlpatterns = format_suffix_patterns(urlpatterns)