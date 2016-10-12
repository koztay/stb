from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from data_importer.models import FileHistory
from data_importer.views import DataImporterForm
from data_importer.importers import XLSImporter, XLSXImporter, XMLImporter
from products.models import Product
from products.mixins import StaffRequiredMixin


# csv importer çalışmıyor. dosyayı text modunda açtın değil mi diye soruyor salak.
# class ExampleCSVImporter(CSVImporter):
#     class Meta:
#         model = Person
#         delimiter = ','
#         ignore_first_line = True


class ImporterHomePageView(StaffRequiredMixin, TemplateView):
    template_name = "importer/importer_list.html"


# TODO : Önce XLS importu başarılı olarak yap sonra Generic olarak genelle.
class ProductXLSImporterModel(XLSImporter):
    class Meta:
        model = Product
        ignore_first_line = True

    # process row'u override edeceğiz.
    # TODO: Burada her Row 'u process ederken task olarak RabbitMQ queue 'ye ekle.
    def process_row(self, row, values):
        print(row, values)


class ProductXLSXImporterModel(XLSXImporter):
    class Meta:

        model = Product
        ignore_first_line = True


class ProductXMLImporterModel(XMLImporter):
    class Meta:
        model = Product
        ignore_first_line = True


class XLSImporterCreateView(DataImporterForm):
        HAS_CELERY = False
        template_name = 'importer/product_importer.html'
        extra_context = {'title': 'Create XLS Data Importer',
                         'template_file': 'myfile.xls',
                         'success_message': "File uploaded successfully"}
        importer = ProductXLSImporterModel


class XLSXImporterCreateView(DataImporterForm):
        template_name = 'importer/product_importer.html'
        extra_context = {'title': 'Create XLSX Data Importer',
                         'template_file': 'myfile.xlsx',
                         'success_message': "File uploaded successfully"}
        importer = ProductXLSXImporterModel


class XMLImporterCreateView(DataImporterForm):
    template_name = 'importer/product_importer.html'
    extra_context = {'title': 'Create XML Data Importer',
                     'template_file': 'myfile.xml',
                     'success_message': "File uploaded successfully"}
    importer = ProductXMLImporterModel


