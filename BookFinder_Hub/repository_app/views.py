from django.shortcuts import render, redirect
from .models import Repository 
# Create your views here.


def repository(request):
    return render(request, 'repository.html', {'books': [1, 2, 3, 4]})
