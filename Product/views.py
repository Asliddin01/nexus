from django.shortcuts import render
from .models import Product, ProductImage
from django.db.models import Prefetch
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from user.models import Profile


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


def product_detail(request, pk, slug=None):
    product = (
        Product.objects
        .select_related('category', 'location', 'brand', 'user')
        .prefetch_related('images')
        .get(pk=pk)
    )
    posted_by = Profile.objects.get(pk=product.user.pk)
    products_by_seller = (
        Product.objects
        .filter(user=product.user)
        .select_related('location', 'brand', 'user')
        .prefetch_related(Prefetch('images', queryset=ProductImage.objects.filter(is_main=True)))
    )
    ctx = {
        "product": product,
        "posted_by": posted_by,
        "products_by_seller": products_by_seller,
    }
    return render(request, 'ads-details.html', ctx)

def product_add(request):
    ctx ={

    }
    return render(request, 'product_add.html', ctx)