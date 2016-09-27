from django.db.models import Sum
from django.views.generic.detail import DetailView

from products.models import Category, Product
from .models import StaticPage


class StaticPageDetailView(DetailView):
    model = StaticPage

    def get_context_data(self, *args, **kwargs):
        context = super(StaticPageDetailView, self).get_context_data(*args, **kwargs)

        categories = Category.objects.all().filter(parent=None).order_by('title')
        most_visited_products = Product.objects.annotate(num_views=Sum('productview__count')).order_by('-num_views')[:3]
        context["categories"] = categories
        context["most_visited_products"] = most_visited_products

        return context
