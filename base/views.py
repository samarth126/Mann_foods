from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def blogs(request):
    return render(request, 'blog.html',{})

def blog_detail(request):
    return render(request, 'blog-details.html',{})