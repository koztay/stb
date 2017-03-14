from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views
from carts.views import CartView, ItemCountView, ItemsView, CheckoutView, CheckoutFinalView
from orders.views import (
    AddressSelectFormView,
    UserAddressCreateView,
    OrderList,
    OrderDetail)


urlpatterns = [

    # url(r'^pages/', include('django.contrib.flatpages.urls')),  # fpr flatpages urls
    # url(r'^(?P<url>.*/)$', views.flatpage, name='flatpage'),  # for displaying flatpages urls in templates
    url(r'^hakkimizda/$', views.flatpage, {'url': '/hakkimizda/'}, name='hakkimizda'),
    # url(r'^license/$', views.flatpage, {'url': '/license/'}, name='license'),
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
    url(r'^api/cart/', include('carts.api.urls', namespace='cart_api')),
    url(r'^api/products/', include('products.api.urls', namespace='products_api')),
    url(r'^cart/count/$', ItemCountView.as_view(), name='item_count'),  # ajax call url
    url(r'^cart/items/$', ItemsView.as_view(), name='items_list'),  # ajax call url
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^checkout/address/$', AddressSelectFormView.as_view(), name='order_address'),
    url(r'^checkout/address/add/$', UserAddressCreateView.as_view(), name='user_address_create'),
    url(r'^checkout/final/$', CheckoutFinalView.as_view(), name='checkout_final'),

    # tiny_mce
    url(r'^tinymce/', include('tinymce.urls')),

    # data-importer
    url(r'^data-importer/', include('importer.urls', namespace='importer')),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # static_pages bu en altta olmazsa yukarıdakiler çalışmıyor.
    # url(r'^(?P<slug>[\w-]+)/$', StaticPageDetailView.as_view(), name='static_page_detail'), # flatpages kullanıyorum

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
