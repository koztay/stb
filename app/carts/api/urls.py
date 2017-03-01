from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import CartItemsListView

urlpatterns = [
    url(r'^$', CartItemsListView.as_view(), name='api_cart_list')  #/api/cart/
]