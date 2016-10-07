from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from products.models import Variation, AttributeType, AttributeValue, Product, Category, Thumbnail, ProductImage
from utils import thumbnail_creator


def product_post_save_receiver_for_variation(sender, instance, created, *args, **kwargs):
    product = instance
    variations = product.variation_set.all()
    if variations.count() == 0:
        new_var = Variation()
        new_var.product = product
        new_var.title = "Default"
        new_var.price = product.price
        new_var.save()


# This receiver function creates predefined product attributes for saced product
def product_post_save_receiver_for_attributes(sender, instance, created, *args, **kwargs):
    product_features = AttributeType.objects.filter(product_type=instance.product_type)
    print(instance.title)
    print("all product features :%s" % product_features)
    assigned_product_features = AttributeType.objects.filter(product=instance)
    print("assigned product features :%s" % assigned_product_features)

    for feature in product_features:
        if feature not in assigned_product_features:
            feature.product.add(instance)
            feature.save()
            # print(feature.product)
            AttributeValue.objects.create(attribute_type=feature, product=instance, value="")
        else:
            # eğer feature producta ekliyse
            # bu durumda feature 'ı al assigned product features a bak değer döndürmeyenleri ekle
            product_attribute_value = AttributeValue.objects.filter(product=instance,
                                                                    attribute_type=feature)
            print(product_attribute_value)
            if product_attribute_value:
                print("bu type eklenmiş.")
                print(product_attribute_value[0])

            else:
                print("bu type eklenecek.")
                AttributeValue.objects.create(attribute_type=feature, product=instance, value="")


# This receiver function creates attribute taypes for existing products after an attribute created
def attribute_type_post_save_receiver(sender, instance, created, *args, **kwargs):
    # 1 - tüm productlar içerisinde product_type 'ı yeni yaratılan attibute'un product_type'ı aynı olanları süz.
    products = Product.objects.filter(product_type=instance.product_type)
    print(products)
    # 2 - süzülen productlara yeni attribute' u ekle:
    for product in products:
        print(instance)
        assigned_product_features = AttributeType.objects.filter(product=product)
        print("assigned product features :%s" % assigned_product_features)
        if instance not in assigned_product_features:
            instance.product.add(product)
            AttributeValue.objects.create(attribute_type=instance, product=product, value="")


def create_slug(instance, sender, new_slug=None):
    print(instance)
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = sender.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, sender=sender, new_slug=new_slug)
    return slug


def productimage_post_save_receiver_for_thumbnail(sender, instance, created, *args, **kwargs):
    if sender:  # bu ilk seferde neden None döndürüyor anlamadım?
        hd, hd_created = Thumbnail.objects.get_or_create(product=instance.product, type='hd')
        sd, sd_created = Thumbnail.objects.get_or_create(product=instance.product, type='sd')
        mid, mid_created = Thumbnail.objects.get_or_create(product=instance.product, type='medium')
        micro, micro_created = Thumbnail.objects.get_or_create(product=instance.product, type='micro')

        # hd_max = (width, height)
        hd_max = (900, 1024)
        sd_max = (500, 600)
        mid_max = (250, 300)
        micro_max = (150, 150)

        media_path = instance.get_image_path()
        owner_slug = instance.product.slug
        if hd_created:
            thumbnail_creator.create_new_thumb(media_path, hd, owner_slug, hd_max[0], hd_max[1])

        if sd_created:
            thumbnail_creator.create_new_thumb(media_path, sd, owner_slug, sd_max[0], sd_max[1])

        if mid_created:
            thumbnail_creator.create_new_thumb(media_path, mid, owner_slug, mid_max[0], mid_max[1])

        if micro_created:
            thumbnail_creator.create_new_thumb(media_path, micro, owner_slug, micro_max[0], micro_max[1])

        # yukarıdaki gibi if 'ler olduğunda sadece ilk resme ilişkin thumnail yaratıyor. Biz tamamı,
        # için thumbnail yaratmak istiyoruz. Ama bu sefer de thumb resme ait mi değil mi bulmamız gerek.

        # thumbnail_creator.create_new_thumb(media_path, hd, owner_slug, hd_max[0], hd_max[1])
        # thumbnail_creator.create_new_thumb(media_path, sd, owner_slug, sd_max[0], sd_max[1])
        # thumbnail_creator.create_new_thumb(media_path, mid, owner_slug, mid_max[0], mid_max[1])
        # thumbnail_creator.create_new_thumb(media_path, micro, owner_slug, micro_max[0], micro_max[1])

post_save.connect(productimage_post_save_receiver_for_thumbnail, sender=ProductImage)
post_save.connect(product_post_save_receiver_for_attributes, sender=Product)
post_save.connect(product_post_save_receiver_for_variation, sender=Product)
post_save.connect(attribute_type_post_save_receiver, sender=AttributeType)


@receiver(pre_save)
def slug_pre_save_receiver(sender, instance, *args, **kwargs):
    print("pre_save_receiver_çalıştı...")

    list_of_models = ('Product', 'Category')
    print("sender:", sender.__name__)

    if sender.__name__ in list_of_models:  # this is the dynamic part you want
        if not instance.slug:
            instance.slug = create_slug(instance, sender)
    else:
        print("sender list of models içinde değil")


#     if sender.__name__ == 'Category':
#         instance.order = instance.id


# @receiver(post_save, sender=Category)
# def category_order_receiver(sender, instance, *args, **kwargs):
#     print("post save category çalışıyor mu?")
#     instance.order = instance.id
#     # instance.save() # bu satır patlatıyor...



