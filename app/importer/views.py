from django.views.generic.base import TemplateView

# from_valid metodunu override edersek aşağıdakiler gerekiyor
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType  # bu neden gerekli?
from data_importer.models import FileHistory


from data_importer.views import DataImporterForm
from data_importer.importers import XMLImporter, GenericImporter  # ileride XMLImporterı da kaldırabilirsek süper olur.
from products.models import Product, ProductType, AttributeType, AttributeValue, Category, ProductImage
from products.mixins import StaffRequiredMixin

from .forms import ProductImporterMapTypeForm, ProductXMLImporterMapRootValueForm
from .models import ProductImportMap, default_fields


def process_xls_row(importer_map, row, values):
    print(row, values)
    # print("I am printing importer_map_type_id: ", self.importer_type)

    # 1-) get product type from row (there must be such column in excel sheet)
    importer_map = importer_map
    print(importer_map.type)

    def get_cell_for_field(field_name):
        try:
            field_object = importer_map.fields_set.get(product_field=field_name)
            cell_value_index = field_object.get_xml_field()  # Adına get_xml_filed demişiz ama xls, xlsx için de aynısı.
            cell_value = values[int(cell_value_index)]  # field eşleştirmeleri 0,1,2 gibi indeks değeri ile yapıldığı
            # için sorun yok. Şimdilik indeks yerine hücreye ait başlık ile eşleştirme yapmayı çözemedim.
        except:
            cell_value = ""
        return cell_value

    # Eğer ürün önceden elkenmişse mevcut filed'ları update etmek için kullanılan fonksiyon.
    def update_default_fields(product_instance=None):
        for field in default_fields:
            cell = get_cell_for_field(field)
            print("field", field)
            if field == "Ürün Adı":
                print("Ürün Adı:", cell)
            elif field == "Ürün Fiyatı":
                print("update price")
                print("Ürün Fiyatı:", cell)
                product_instance.price = cell  # bu değer text olarak geliyor.
            elif field == "Ürün Tanımı":
                print("Ürün Tanımı:", cell)
                product_instance.description = cell
            elif field == "Ürün Kategorisi":
                print("Ürün Kategorisi:", cell)
                try:
                    category = Category.objects.get(title=cell)
                    product_instance.default = category
                except:
                    print('Category bulunamadı.')
            elif field == "Ürün Resmi":
                print("Ürün Resmi:", cell)

            else:
                print("this field will be updated as attribute value")
        product_instance.valueset = values
        product_instance.importer_map = importer_map
        print("product_instance.valueset", product_instance.valueset)
        product_instance.save()  # burada gönderdiğim values yazılacak mı bakalım?

    title = get_cell_for_field("Ürün Adı")
    product_type = ProductType.objects.get(name=importer_map.type)
    # aşağıda product yaratılınca aynı zamanda da save ediliyor ama bu sefer importer_map gönderilmiyor.
    product, product_created = Product.objects.get_or_create(title=title, product_type=product_type)
    # aşağıda ise importer_map gönderiliyor.
    update_default_fields(product)  # her halükarda yaratılacak o yüzden önemsiz...


class ImporterHomePageView(StaffRequiredMixin, TemplateView):
    template_name = "importer/importer_list.html"


class ProductGenericImporter(GenericImporter):
    class Meta:
        model = Product
        ignore_first_line = True

    # process row'u override edeceğiz. kendi importerımı kendim yazıyorum.
    # TODO: Burada her Row 'u process ederken task olarak RabbitMQ queue 'ye ekle.
    def process_row(self, row, values):
        importer_map = ProductImportMap.objects.get(pk=self.importer_type)
        process_xls_row(importer_map=importer_map, row=row, values=values)


class GenericImporterCreateView(DataImporterForm):

    template_name = 'importer/product_importer.html'
    extra_context = {'title': 'Select File for Data Importer',
                     'template_file': 'myfile.xls',
                     'success_message': "File uploaded successfully",
                     }
    importer = ProductGenericImporter

    def get_context_data(self, **kwargs):
        context = super(GenericImporterCreateView, self).get_context_data(**kwargs)
        importer_type_form = ProductImporterMapTypeForm(self.request.POST or None)
        context['importer_type_form'] = importer_type_form
        return context

    def form_valid(self, form, owner=None):
        selected_import_map_id = self.request.POST.get('import_map')  # import map seçebilmek için.
        self.importer.importer_type = selected_import_map_id

        if self.request.user.id:
            owner = self.request.user

        if self.importer.Meta.model:
            content_type = ContentType.objects.get_for_model(self.importer.Meta.model)
            file_history, _ = FileHistory.objects.get_or_create(file_upload=form.cleaned_data['file_upload'],
                                                                owner=owner,
                                                                content_type=content_type)
        # Bu satırı celery 'yi dikkate almaması için yazdık.
        self.is_task = False
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
