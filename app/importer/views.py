from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
# from django.contrib import messages
# from django.contrib.contenttypes.models import ContentType
# from data_importer.models import FileHistory
from data_importer.views import DataImporterForm
from data_importer.importers import XLSImporter, XLSXImporter, XMLImporter
from products.models import Product
from products.mixins import StaffRequiredMixin

from .models import ProductImportMap, Fields

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

    # process row'u override edeceğiz. kendi importerımı kendim yazıyorum.
    # TODO: Burada her Row 'u process ederken task olarak RabbitMQ queue 'ye ekle.
    def process_row(self, row, values):
        print(row, values)

        # 1-) get product type from row (there must be such column in excel sheet)
        # 1 - a) get importer name from row (there must be such column in excel sheet)
        # (importer name bilgisinden mapping 'e ulaşabiliriz.)

        # 2-) get all attribute types for product type

        # 3-) get column headers from product type for attribute types
        # this can be get from models which describes matching schema for importer

        # 4-) get column values from row by using importer schema (get it from the importer name column)

        # 5-) get or create product

        # 6-) get or create attribute values (not types, types must be created manually)

        # 7-) update all (product.attribute_type = bla_bla, product.attribute_value = bla_bla)

        # 8-) save product


class ProductXLSXImporterModel(XLSXImporter):
    class Meta:

        model = Product
        ignore_first_line = True


class ProductXMLImporterModel(XMLImporter):
    class Meta:
        model = Product
        ignore_first_line = True


class XLSImporterCreateView(DataImporterForm):
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


