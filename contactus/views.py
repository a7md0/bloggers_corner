from django.shortcuts import render
from django.http import HttpResponse
from contactus.forms import ContactusForm

# Create your views here.
def contactus(request):
    myForm = ContactusForm()

    return render(request, 'contactus/contactus.html', { 'myForm': myForm })
