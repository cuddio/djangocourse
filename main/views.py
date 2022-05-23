from django.shortcuts import render
from .models import Tour

def index(request):
    tours = Tour.objects.all()
    return render(request, 'index.html', {'tours': tours})
