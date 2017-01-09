from __future__ import absolute_import, unicode_literals
from celery.decorators import task

from .models import default_fields, ProductImportMap
from products.models import Product, Variation, ProductType


@task(name="Process XLS Row")
def process_xls_row(importer_map_pk, row, values):
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
        variation_instance = product_instance.variation_set.all()[0]  # product save edilince otomatik yaratılmış olmalı.
        for main_field in default_fields:
            cell = get_cell_for_field(main_field)
            print("cell_value :", cell)
            cell_value_model = default_fields[main_field]["model"]
            print("cell_value_model: ", cell_value_model)
            if cell_value_model is "Product":
                print("attribute: ", default_fields[main_field]["field"])
                print("value: ", cell)
                setattr(product_instance, default_fields[main_field]["field"], cell)
            elif cell_value_model is "Variation":
                print("attribute: ", default_fields[main_field]["field"])
                print("value: ", cell)
                setattr(variation_instance, default_fields[main_field]["field"], cell)
            elif cell_value_model is "ProductType":
                # product_type_name = default_fields[main_field]["field"]
                # print("product_type_name :", product_type_name)

                product_type_instance, created = ProductType.objects.get_or_create(name=cell)
                product_instance.product_type = product_type_instance
            else:
                print("Hata! Böyle bir model dönmemeli")
        product_instance.price = variation_instance.sale_price  # ürünlerin fiyatı boş geliyor o nedenle...
        product_instance.save()
        variation_instance.save()

    title = get_cell_for_field("Ürün Adı")
    # product_type = ProductType.objects.get(name=importer_map.type)
    product, product_created = Product.objects.get_or_create(title=title)

    update_default_fields(product_instance=product)
    # update_default_fields(product)  # her halükarda yaratılacak o yüzden önemsiz...
    return "% update edildi." % product.title


