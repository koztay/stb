from django.conf.urls import url

from .views import DataImporterCreateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    # url(r'^$', 'products.views.product_list', name='products'),
    url(r'^$', DataImporterCreateView.as_view(), name='product_importer'),
    # url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='product_detail'),
]
