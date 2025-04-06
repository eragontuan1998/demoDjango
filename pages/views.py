from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePageView(request):
    print("View function called")
    return HttpResponse("Hello, World!")