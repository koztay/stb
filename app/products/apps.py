from django.apps import AppConfig


class ProductsAppConfig(AppConfig):
    name = 'products'
    verbose_name = 'Products'

    def ready(self):
        # import signal handlers # aşağıdaki satırdaki gibi signals import edilmezse hiçbir
        # signal çalışmıyor...
        pass