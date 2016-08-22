from django.contrib import admin
from .models import SliderImage, Promotion, PromotionThumbnail


class PromotionThumbnailInline(admin.TabularInline):
    extra = 1
    model = PromotionThumbnail


class PromotionAdmin(admin.ModelAdmin):
    inlines = [
        PromotionThumbnailInline,
    ]

    class Meta:
        model = Promotion

admin.site.register(SliderImage)
admin.site.register(Promotion, PromotionAdmin)
