from django.shortcuts import render
from django.http import request, response
from django.shortcuts import render, redirect
# Create your views here.


def home(request):
    return render(request, 'app/index.html', {})