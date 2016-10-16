from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView

# from_valid metodunu override edersek aşağıdakiler gerekiyor
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from data_importer.models import FileHistory


from data_importer.views import DataImporterForm
from data_importer.importers import XLSImporter, XLSXImporter, XMLImporter
from products.models import Product, ProductType, AttributeType, AttributeValue, Category, ProductImage
from products.mixins import StaffRequiredMixin

from .forms import ProductImporterMapTypeForm
from .models import ProductImportMap, default_fields

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
        # print("I am printing importer_map_type_id: ", self.importer_type)

        # 1-) get product type from row (there must be such column in excel sheet)
        importer_map = ProductImportMap.objects.get(pk=self.importer_type)
        print(importer_map.type)

        def get_cell_for_field(field_name):
            try:
                field_object = importer_map.fields_set.get(product_field=field_name)
                cell_value_index = int(field_object.get_xml_field())
                cell_value = values[cell_value_index]
            except:
                return None
            return cell_value

        def update_default_fields(update_product=None):
            for field in default_fields:
                cell = get_cell_for_field(field)
                print("field", field)
                if field == "Ürün Adı":
                    print("do nothing")
                elif field == "Ürün Fiyatı":
                    print("update price")
                    update_product.price = cell
                    # product.save()
                elif field == "Ürün Tanımı":
                    print("update description")
                    update_product.description = cell
                    # product.save()
                elif field == "Ürün Kategorisi":
                    print("update category")
                    category = Category.objects.get(title=cell)
                    update_product.default = category
                elif field == "Ürün Resmi":
                    print("update picture şimdilik birşey yapma")

                else:
                    print("this field will be updated as attribute value")
            update_product.save()

        def update_attribute_fields(update_product=None):
            attribute_types = AttributeType.objects.filter(product=update_product)
            # attributes_to_update = AttributeValue.objects.filter(attribute_type=attribute_type)
            print(attribute_types)
            for attr_type in attribute_types:
                type_name = attr_type.type
                type_value = get_cell_for_field(type_name)
                attr_value, created_or_not = AttributeValue.objects.get_or_create(value=type_value, attribute_type=attr_type)
                attr_value.product = update_product
                attr_value.save()
                # attr_type.attributevalue_set.get_or_create(attr_value)

        title = get_cell_for_field("Ürün Adı")
        product_type = ProductType.objects.get(name=importer_map.type)
        product, created = Product.objects.get_or_create(title=title, product_type=product_type)

        update_default_fields(product)  # her halükarda yaratılacak o yüzden önemsiz...
        update_attribute_fields(product)

        # except:
        #     print("yukarıdaki lerden herhangi biri sağlanamadı...")

        # for field in fields:
        #     print(field.product_field, field.xml_field)
        #     try:
        #         attribute_type = AttributeType.objects.get(type=field.product_field, product=product)
        #         print(attribute_type)
        #         # attribute_type.product = product
        #         # attribute_type.save()
        #     except:
        #         print("attribute_type bulunamadı")
        #     print(values)
        #     attribute_cell_value = values[int(field.xml_field)]
        #     print("attribute_cell_value:", attribute_cell_value)
        #     print("attribute_type", attribute_type)
        #     print("product", product)
        #     attribute_value, created = AttributeValue.objects.get_or_create(value=attribute_cell_value,
        #                                                                     attribute_type=attribute_type,
        #                                                                     product=product)



class ProductXLSXImporterModel(XLSXImporter):
    class Meta:

        model = Product
        ignore_first_line = True


class ProductXMLImporterModel(XMLImporter):
    importer_type = None

    class Meta:
        model = Product
        ignore_first_line = True


class XLSImporterCreateView(DataImporterForm):

    template_name = 'importer/product_importer.html'
    extra_context = {'title': 'Create XLS Data Importer',
                     'template_file': 'myfile.xls',
                     'success_message': "File uploaded successfully",
                     }
    importer = ProductXLSImporterModel

    def get_context_data(self, **kwargs):
        context = super(XLSImporterCreateView, self).get_context_data(**kwargs)
        importer_type_form = ProductImporterMapTypeForm(self.request.POST or None)
        context['importer_type_form'] = importer_type_form
        return context

    def form_valid(self, form, owner=None):
        selected_import_map_id = self.request.POST.get('import_map')
        self.importer.importer_type = selected_import_map_id

        if self.request.user.id:
            owner = self.request.user

        if self.importer.Meta.model:
            content_type = ContentType.objects.get_for_model(self.importer.Meta.model)
            file_history, _ = FileHistory.objects.get_or_create(file_upload=form.cleaned_data['file_upload'],
                                                                owner=owner,
                                                                content_type=content_type)

        if not self.is_task or not hasattr(self.task, 'delay'):
            self.task.run(importer=self.importer,
                          source=file_history,
                          owner=owner,
                          send_email=False)
            if self.task.parser.errors:
                messages.error(self.request, self.task.parser.errors)
            else:
                messages.success(self.request,
                                 self.extra_context.get('success_message', "File uploaded successfully"))
        else:
            self.task.delay(importer=self.importer, source=file_history, owner=owner)
            if owner:
                messages.info(
                    self.request,
                    "When importer was finished one email will send to: {0!s}".format(owner.email)
                )
            else:
                messages.info(
                    self.request,
                    "Importer task in queue"
                )

        return super(DataImporterForm, self).form_valid(form)


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


