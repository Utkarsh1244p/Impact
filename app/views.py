from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blogDetails(request):
    return render(request, 'blog-details.html', {})
