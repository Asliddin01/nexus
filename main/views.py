from django.shortcuts import render
from category.models import Category, Region
from Product.models import Product, ProductImage
from django.db.models import Prefetch
from blog.models import Blog

def main(request):
    categories = Category.objects.filter(is_main = True)
    region = Region.objects.all()
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
    ctx= { "categories" : categories,
            "region" : region,
            "products" : products
          }
    blogs = Blog.objects.order_by('-created_at')[:3].select_related("user")

    return render(request, 'index-2.html', ctx)
# Create your views here.

def contact(request):
    ctx = {}
    return render(request, 'contact.html', ctx)

def services(request):
    ctx = {}
    return render(request, 'services.html', ctx)
def about(request):
    ctx = {}
    return render(request, 'about.html', ctx)

