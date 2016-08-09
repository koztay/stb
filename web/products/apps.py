from django.apps import AppConfig


class ProductsAppConfig(AppConfig):
    name = 'products'
    verbose_name = 'Products'

    def ready(self):
        # import signal handlers
        pass
