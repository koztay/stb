from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from carts.views import CartView, ItemCountView, CheckoutView, CheckoutFinalView
from orders.views import (
    AddressSelectFormView,
    UserAddressCreateView,
    OrderList,
    OrderDetail)

from static_pages.views import StaticPageDetailView

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    # url(r'^about/$', 'ecommerce2.views.about', name='about'),


    url(r'^istebu_backend_1357/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^categories/', include('products.urls_categories', namespace='categories')),
    url(r'^orders/$', OrderList.as_view(), name='orders'),
    url(r'^orders/(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^cart/count/$', ItemCountView.as_view(), name='item_count'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^checkout/address/$', AddressSelectFormView.as_view(), name='order_address'),
    url(r'^checkout/address/add/$', UserAddressCreateView.as_view(), name='user_address_create'),
    url(r'^checkout/final/$', CheckoutFinalView.as_view(), name='checkout_final'),

    # static_pages
    url(r'^(?P<slug>[\w-]+)/$', StaticPageDetailView.as_view(), name='static_page_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
