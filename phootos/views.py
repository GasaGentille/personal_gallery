from django.shortcuts import render
from .models import Image, Location , Category
# from django.http  import HttpResponse

# Create your views here.


def image(request):
    return  render (request,'image.html')
    
