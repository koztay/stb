from django.contrib import admin

from .models import Product, Variation, ProductImage, Category, ProductFeatured, AttributeType, AttributeValue, \
    ProductType, Thumbnail


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    max_num = 10


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0
    max_num = 10


class AttributeTypeInline(admin.TabularInline):
    model = AttributeType
    extra = 0
    ordering = ("order",)


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 0
    ordering = ("attribute_type__order",)


# class ProductTypeInline(admin.TabularInline):
#     model = ProductType


class AttributeTypeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'product_type', 'order']
    list_editable = ['order']
    fields = ('product_type', 'type', 'product', 'order',)
    ordering = ("product_type", 'order',)
    list_filter = ("product_type",)

    # inlines = [ProductTypeInline, ]  # No ForeignKey Hatası veriyor.
    # exclude = ('product',)

    class Meta:
        model = AttributeType
        order_by = 'order'


class ThumbnailInline(admin.TabularInline):
    extra = 1
    model = Thumbnail


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price']
    inlines = [
        ProductImageInline,
        ThumbnailInline,
        VariationInline,
        AttributeValueInline,
    ]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

# admin.site.register(Variation)

admin.site.register(ProductImage)

admin.site.register(Category)

admin.site.register(ProductFeatured)

admin.site.register(ProductType)
admin.site.register(AttributeType, AttributeTypeAdmin)
admin.site.register(AttributeValue)
