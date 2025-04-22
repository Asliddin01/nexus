from django.urls import path
from .views import get_list_ptg, detail_ptg

urlpatterns = [
    path('', get_list_ptg, name='product-list'),
    path('<int:pk>/', detail_ptg, name='detail-ptg')
]
