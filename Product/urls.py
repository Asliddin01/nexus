from django.urls import path
from .views import product_list, product_detail, product_add

urlpatterns = [
    path('list/', product_list, name='product-list'),
    path('<int:pk>/>', product_detail, name="product_detail"),
    path('product_add', product_add, name='product-add'),
    
]