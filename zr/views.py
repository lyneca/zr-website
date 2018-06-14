from django.shortcuts import render
from .models import Question

# Create your views here.

def index(request):
    return render(request, "zr/index.html")

def qanda(request):
    context = {
        "questions": Question.objects.all()
    }
    return render(request, "zr/qanda.html", context=context)
