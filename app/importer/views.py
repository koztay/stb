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


class ProductXLSImporterModel(XLSImporter):
    class Meta:
        model = Product
        ignore_first_line = True


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

        def form_valid(self, form, owner=None):

            if self.request.user.id:
                owner = self.request.user

            if self.importer.Meta.model:
                content_type = ContentType.objects.get_for_model(self.importer.Meta.model)
                print('cleaned_data:', form.cleaned_data)
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
                        "When importer was finished one email will send to: %s" % owner.email
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

        # def form_valid(self, form, owner=None):
        #     # burada objeleri alıp database'de varsa update edeceğiz.
        #     return super(DataImporterForm, self).form_valid(form)


class XMLImporterCreateView(DataImporterForm):
    template_name = 'importer/product_importer.html'
    extra_context = {'title': 'Create XML Data Importer',
                     'template_file': 'myfile.xml',
                     'success_message': "File uploaded successfully"}
    importer = ProductXMLImporterModel

    # def form_valid(self, form, owner=None):
    #     # burada objeleri alıp database'de varsa update edeceğiz.
    #     return super(DataImporterForm, self).form_valid(form)
