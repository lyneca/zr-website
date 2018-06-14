from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('qanda', qanda, name='qanda'),
]
