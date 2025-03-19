from django.shortcuts import render
from .models import Product, ProductImage
from django.db.models import Prefetch
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product_list(request):
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images')
    )

    paginator = Paginator(products, 1)  

    page = request.GET.get("page")

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1) 
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages) 
    ctx = {
        "products": page_obj,
    }
    return render(request, 'product.html', ctx)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    ctx = {

    }
    return render(request, 'detail.html', ctx)