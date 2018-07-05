from .views import index, about, resources, qanda, contact
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('resources', resources, name='resources'),
    path('qanda', qanda, name='qanda'),
    path('contact', contact, name='contact'),
]
