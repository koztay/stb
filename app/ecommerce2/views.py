from django.db.models import Sum
from django.shortcuts import render

from products.models import Category, Product


# def about(request):
#     categories = Category.objects.all().filter(parent=None).order_by('title')
#     most_visited_products = Product.objects.annotate(num_views=Sum('productview__count')).order_by('-num_views')[:3]
#
#     context = {
#         'categories': categories,
#         'most_visited_products': most_visited_products,
#
#     }
#
#     return render(request, "about.html", context)
