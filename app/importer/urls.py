from django.conf.urls import url

from .views import XLSImporterCreateView, XLSXImporterCreateView, XMLImporterCreateView, ImporterHomePageView

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    # url(r'^$', 'products.views.product_list', name='products'),
    url(r'^$', ImporterHomePageView.as_view(), name='product_importer_home'),
    url(r'^XLS/$', XLSImporterCreateView.as_view(), name='xls_importer'),
    url(r'^XLSX/$', XLSXImporterCreateView.as_view(), name='xlsx_importer'),
    url(r'^XML/$', XMLImporterCreateView.as_view(), name='xml_importer'),
]
