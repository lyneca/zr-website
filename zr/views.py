from django.shortcuts import render
from .models import Question

# Create your views here.

def index(request):
    return render(request, "zr/index.html")

def about(request):
    return render(request, "zr/about.html")

def media(request):
    return render(request, "zr/media.html")

def resources(request):
    return render(request, "zr/resources.html")

def qanda(request):
    context = {
        "questions": Question.objects.all()
    }
    return render(request, "zr/qanda.html", context=context)

def contact(request):
    return render(request, "zr/contact.html")
