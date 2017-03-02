from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CartItemsListView, CartDetailView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', CartDetailView.as_view()),
    url(r'^$', CartItemsListView.as_view(), name='api_cart_list'),  # /api/cart/

]

urlpatterns = format_suffix_patterns(urlpatterns)