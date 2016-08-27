from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify

# from utils import thumbnail_location, THUMB_CHOICES


def thumbnail_location(instance, filename):
    return "products/%s/thumbnails/%s" % (instance.product.slug, filename)

THUMB_CHOICES = (
    ("hd", "HD"),
    ("sd", "SD"),
    ("micro", "Micro"),
)


# This utility function creates the filename and filepath according to the slug and product instance
def image_upload_to(instance, filename):
    title = instance.product.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" % (slug, instance.id, file_extension)
    return "products/%s/%s" % (slug, new_filename)


# This utility function creates the filename and filepath according to the slug and product instance
def image_upload_to_featured(instance, filename):
    title = instance.product.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" % (slug, instance.id, file_extension)
    return "products/%s/featured/%s" % (slug, new_filename)


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()

    def get_related(self, instance):
        products_one = self.get_queryset().filter(categories__in=instance.categories.all())
        products_two = self.get_queryset().filter(default=instance.default)
        qs = (products_one | products_two).exclude(id=instance.id).distinct()
        return qs


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', blank=True)
    product_type = models.ForeignKey('ProductType', null=True, blank=True)
    # attribute_type = models.ManyToManyField('AttributeType')
    default = models.ForeignKey('Category', related_name='default_category', null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)  # unique=True)

    objects = ProductManager()

    class Meta:
        ordering = ["-title"]

    def __str__(self):  # def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("products:product_detail", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        view_name = "products:product_detail_slug_function"
        return reverse(view_name, kwargs={"slug": self.slug})
        #
        # def get_image_url(self): # buna gerek yok o zaman
        #     img = self.productimage_set.first()
        #     if img:
        #         return img.image.url
        #     return img  # None


class Variation(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    sale_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(null=True, blank=True)  # refer none == unlimited amount

    def __str__(self):
        return self.title

    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.price

    def get_html_price(self):
        if self.sale_price is not None:
            html_text = "<span class='sale-price'>%s</span> <span class='og-price'>%s</span>" % (self.sale_price,
                                                                                                 self.price)
        else:
            html_text = "<span class='price'>%s</span>" % self.price
        return mark_safe(html_text)

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def add_to_cart(self):
        return "%s?item=%s&qty=1" % (reverse("cart"), self.id)

    def remove_from_cart(self):
        return "%s?item=%s&qty=1&delete=True" % (reverse("cart"), self.id)

    def get_title(self):
        return "%s - %s" % (self.product.title, self.title)


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to=image_upload_to)

    def get_image_path(self):
        # img = self.image

        img_url = self.image.url
        # remove MEDIA_URL from img_url
        img_url = img_url.replace(settings.MEDIA_URL, "/", 1)
        # combine with media_root
        img_path = settings.MEDIA_ROOT + img_url
        if img_url:
            return img_path
        return img_path  # None

    def __str__(self):
        return self.product.title


# Product Category
class Category(models.Model):
    parent = models.ForeignKey("self", null=True, blank=True)
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    show_on_homepage = models.BooleanField(default=True)
    order = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("categories:category_detail", kwargs={"slug": self.slug})

    @property
    def is_child(self):
        if self.parent is not None:
            return True
        else:
            return False

    def get_children(self):
        if self.is_child:
            return None
        else:
            return Category.objects.filter(parent=self)


class ProductFeatured(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to=image_upload_to_featured)
    title = models.CharField(max_length=120, null=True, blank=True)
    text = models.CharField(max_length=220, null=True, blank=True)
    text_right = models.BooleanField(default=False)
    text_css_color = models.CharField(max_length=6, null=True, blank=True)
    show_price = models.BooleanField(default=False)
    make_image_background = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.title


class ProductType(models.Model):
    name = models.CharField(max_length=120, default="Projeksiyon Cihazı")

    def __str__(self):
        return self.name


class AttributeType(models.Model):
    product_type = models.ForeignKey(ProductType)
    order = models.IntegerField(default=0)
    product = models.ManyToManyField(Product, blank=True)
    type = models.CharField(max_length=120)

    def __str__(self):
        return self.type


class AttributeValue(models.Model):
    attribute_type = models.ForeignKey(AttributeType, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    value = models.CharField(max_length=120, default="")

    def __str__(self):
        return self.value


class Thumbnail(models.Model):
    product = models.ForeignKey(Product)  # instance.product.title
    type = models.CharField(max_length=20, choices=THUMB_CHOICES, default='hd')
    height = models.CharField(max_length=20, null=True, blank=True)
    width = models.CharField(max_length=20, null=True, blank=True)
    media = models.ImageField(
        width_field="width",
        height_field="height",
        blank=True,
        null=True,
        upload_to=thumbnail_location)

    def __unicode__(self):  # __str__(self):
        return str(self.media.path)


"""
This way you have a clear picture of how each attribute relates to some vehicle.

Forms

Basically, with this database design, you would require two forms for adding objects into the
database. Specifically a model form for a vehicle and a model formset for attributes.
You could use jQuery to dynamically add more items on the Attribute formset.

Note

You could also separate Attribute class to AttributeType and AttributeValue so you don't have
redundant attribute types stored in your database or if you want to limit the attribute choices
for the user but keep the ability to add more types with Django admin site.

To be totally cool, you could use autocomplete on your form to suggest existing attribute types to the user.

Hint: learn more about database normalization.

"""

"""
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
"""
