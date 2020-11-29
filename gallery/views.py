from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gallery_list(request):
    return HttpResponse("a HTML page should be returned")
