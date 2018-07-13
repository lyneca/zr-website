from .views import index, about, resources, qanda, contact, media
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('resources', resources, name='resources'),
    path('media', media, name='media'),
    path('qanda', qanda, name='qanda'),
    path('contact', contact, name='contact'),
]
