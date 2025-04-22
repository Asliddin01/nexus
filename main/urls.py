from .views import main, contact, services, about
from django.urls import path , include

urlpatterns = [
    path('', main, name = 'main'),
    path('contact/', contact, name = 'contact'),
    path('services/', services, name= 'services' ),
    path('about/', about, name= 'about' )
    
]
