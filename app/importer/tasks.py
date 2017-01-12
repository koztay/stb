from __future__ import absolute_import, unicode_literals
from celery.decorators import task

from .models import default_fields, ProductImportMap
from products.models import Product, ProductType, Currency

# TODO: Currency ve Product Type, Barkod vb. field ları için Validation ekle.

# TODO: http://stackoverflow.com/questions/11618390/celery-having-sequential-tasks-rather-than-concurrent
"""
Single worker consuming from a queue with concurrency equals to one ensures that the tasks will be processed in
sequential order. In other words you can create a special queue and run only one celery worker with concurrency
equals to one:

celery -A tasks worker -Q amazon_queue -c 1
And submit tasks to that queue:

tasks.add.apply_async(args=[1,2], kwargs={}, queue='amazon_queue')
Or use automatic routing for certain task types.
"""

# Udemy Complete Object Bootcamp" - "Jose PORTILLA"
# TODO: Aşağıdaki fonksiyonda "list comprehension" kullanılabilir mi? - LECTURE 37
# TODO: Aşağıdaki fonksiyonda "lambda expressions" kullanılabilir mi? get_cell_for_field() 'da kesin kullanılır. - L42
# TODO: Aşağıdaki fonksiyonda "map", "reduce", "filter", zip kullanılabilir mi? lambda ile birlikte - L71,72,73,74

# ins = [x for x in instance_list if type(x).__name__=="int"]
# instance = lambda modelstring, instancelist: [x for x in instance_list if type(x).__name__==modelstring][0]
# yukarıdaki iki fonksiyon da çalıştı.


# This task has been added for testing purposes.
@task(name="sum_two_numbers")
def add(x, y):
    return x + y


@task(name="Process XLS Row")
def process_xls_row(importer_map_pk, row, values):  # Bu fonksiyonun no_task olarak viewws 'da çalıştığı görüldü.
    # Ancak task olarak çalışıp çalışmadığı test edilemedi.
    """
    Please do not forget to create worker with the folloeşng command, in command line:
    celery -A ecommerce2 worker -l info
    """
    # pydevd.settrace('192.168.1.22', port=5678, stdoutToServer=True, stderrToServer=True)
    importer_map = ProductImportMap.objects.get(pk=importer_map_pk)

    def get_cell_for_field(field_name):
        try:
            field_object = importer_map.fields_set.get(product_field=field_name)
            cell_value_index = field_object.get_xml_field()  # Adına get_xml_filed demişiz ama xls, xlsx için de aynısı.

            cell_value = values[int(cell_value_index)]  # field eşleştirmeleri 0,1,2 gibi indeks değeri ile yapıldığı
            # için sorun yok. Şimdilik indeks yerine hücreye ait başlık ile eşleştirme yapmayı çözemedim.
        except:
            cell_value = ""
        return cell_value

    def update_default_fields(product_instance=None):
        variation_instance = product_instance.variation_set.all()[0]  # product save edilince otomatik yaratılıyor.
        for main_field in default_fields:
            cell = get_cell_for_field(main_field)
            print("cell_value :", cell)
            cell_value_model = default_fields[main_field]["model"]
            print("cell_value_model: ", cell_value_model)

            if cell_value_model is "Product":
                print("attribute: ", default_fields[main_field]["field"])
                print("value: ", cell)
                attribute = default_fields[main_field]["field"]
                if attribute is 'categories':
                    pass
                else:
                    setattr(product_instance, attribute, cell)

            elif cell_value_model is "Variation":
                print("attribute: ", default_fields[main_field]["field"])
                print("value: ", cell)
                setattr(variation_instance, default_fields[main_field]["field"], cell)

            elif cell_value_model is "ProductType":
                # product_type_name = default_fields[main_field]["field"]
                # print("product_type_name :", product_type_name)
                product_type_instance, created = ProductType.objects.get_or_create(name=cell)
                product_instance.product_type = product_type_instance

            elif cell_value_model is "Currency":
                print("attribute: ", default_fields[main_field]["field"])
                print("value: ", cell)
                # Eğer currency veriatabanında yoksa o zaman ürünü ekleme. Dolayısıyla "Para Birimi" önceden eklenmeli.
                try:
                    currency_instance = Currency.objects.get(name=cell)
                except:
                    print("Currency bulunamadı, %s eklenmedi!" % product.title)
                    pass
                variation_instance.buying_currency = currency_instance
                print("variation_instance.buying_currency", variation_instance.buying_currency)

            else:
                print("Hata! Böyle bir model dönmemeli, cell_value_model: ", cell_value_model)
        product_instance.price = variation_instance.sale_price  # ürünlerin fiyatı boş geliyor o nedenle...
        product_instance.save()
        variation_instance.save()

    title = get_cell_for_field("Ürün Adı")
    # product_type = ProductType.objects.get(name=importer_map.type)
    product, product_created = Product.objects.get_or_create(title=title)

    update_default_fields(product_instance=product)
    # update_default_fields(product)  # her halükarda yaratılacak o yüzden önemsiz...
    return "%s update edildi." % product.title



