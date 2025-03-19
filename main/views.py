from django.shortcuts import render
from category.models import Category, Region
from Product.models import Product, ProductImage
from django.db.models import Prefetch
def main(request):
    categories = Category.objects.filter(is_main = True)
    region = Region.objects.all()
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
    ctx= { "categories" : categories,
            "region" : region,
            "products" : products
          }
    return render(request, 'index-2.html', ctx)
# Create your views here.
