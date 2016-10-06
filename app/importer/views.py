from data_importer.views import DataImporterForm
from data_importer.importers import XLSImporter
from products.models import Product


# csv importer çalışmıyor. dosyayı text modunda açtın değil mi diye soruyor salak.
# class ExampleCSVImporter(CSVImporter):
#     class Meta:
#         model = Person
#         delimiter = ','
#         ignore_first_line = True


class ProductXLSImporterModel(XLSImporter):
    class Meta:
        model = Product
        ignore_first_line = True


class DataImporterCreateView(DataImporterForm):
        template_name = 'product_importer.html'
        extra_context = {'title': 'Create Product Data Importer',
                         'template_file': 'myfile.csv',
                         'success_message': "File uploaded successfully"}
        importer = ProductXLSImporterModel
