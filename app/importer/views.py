from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView

# from_valid metodunu override edersek aşağıdakiler gerekiyor
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from data_importer.models import FileHistory


from data_importer.views import DataImporterForm
from data_importer.importers import XLSImporter, XLSXImporter, XMLImporter, GenericImporter
from products.models import Product, ProductType, AttributeType, AttributeValue, Category, ProductImage
from products.mixins import StaffRequiredMixin

from .forms import ProductImporterMapTypeForm, ProductXMLImporterMapRootValueForm
from .models import ProductImportMap, default_fields

# csv importer çalışmıyor. dosyayı text modunda açtın değil mi diye soruyor salak.
# class ExampleCSVImporter(CSVImporter):
#     class Meta:
#         model = Person
#         delimiter = ','
#         ignore_first_line = True


def process_xls_row(importer_map, row, values):
    print(row, values)
    # print("I am printing importer_map_type_id: ", self.importer_type)

    # 1-) get product type from row (there must be such column in excel sheet)
    importer_map = importer_map
    print(importer_map.type)

    def get_cell_for_field(field_name):
        try:
            field_object = importer_map.fields_set.get(product_field=field_name)
            cell_value_index = int(field_object.get_xml_field())
            cell_value = values[cell_value_index]
        except:
            cell_value = ""
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
        update_product.valueset = values
        update_product.importer_map = importer_map
        print("update_product.valueset", update_product.valueset)
        update_product.save()  # burada gönderdiğim values yazılacak mı bakalım?

    title = get_cell_for_field("Ürün Adı")
    product_type = ProductType.objects.get(name=importer_map.type)
    # aşağıda product yaratılınca aynı zamanda da save ediliyor ama bu sefer importer_map gönderilmiyor.
    product, product_created = Product.objects.get_or_create(title=title, product_type=product_type)
    # aşağıda ise importer_map gönderiliyor.
    update_default_fields(product)  # her halükarda yaratılacak o yüzden önemsiz...


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
        importer_map = ProductImportMap.objects.get(pk=self.importer_type)
        process_xls_row(importer_map=importer_map, row=row, values=values)


class ProductXLSXImporterModel(XLSXImporter):
    class Meta:

        model = Product
        ignore_first_line = True

    def process_row(self, row, values):
        importer_map = ProductImportMap.objects.get(pk=self.importer_type)
        process_xls_row(importer_map=importer_map, row=row, values=values)


# >>> from data_importer.importers import XMLImporter
# >>> from data_importer.model import MyModel
# >>> class MyCSVImporterModel(XMLImporter):
# ...     root = 'file'
# ...     class Meta:
# ...         model = MyModel

class ProductXMLImporterModel(GenericImporter):
    root = 'entry'
    # XML 'de root belirtiyoruz. Ona göre process ediyor sanırım. Kompleks
    # XML 'leri nasıl alıyoruz acaba?

    class Meta:
        model = Product

    def process_row(self, row, values):
        print(row, values)
        importer_map = ProductImportMap.objects.get(pk=self.importer_type)
        process_xls_row(importer_map=importer_map, row=row, values=values)


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

    def get_context_data(self, **kwargs):
        context = super(XLSXImporterCreateView, self).get_context_data(**kwargs)
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


class XMLImporterCreateView(DataImporterForm):
    template_name = 'importer/product_importer.html'
    extra_context = {'title': 'Create XML Data Importer',
                     'template_file': 'myfile.xml',
                     'success_message': "File uploaded successfully"}
    importer = ProductXMLImporterModel

    def get_context_data(self, **kwargs):
        context = super(XMLImporterCreateView, self).get_context_data(**kwargs)
        importer_type_form = ProductImporterMapTypeForm(self.request.POST or None)
        context['importer_type_form'] = importer_type_form
        return context

    def form_valid(self, form, owner=None):
        selected_import_map_id = self.request.POST.get('import_map')
        selected_map = ProductImportMap.objects.get(pk=selected_import_map_id)
        root_value = selected_map.root
        self.importer.importer_type = selected_import_map_id
        self.importer.root = root_value
        print(root_value)

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


