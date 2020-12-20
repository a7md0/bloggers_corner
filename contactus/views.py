from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from contactus.forms import ContactusForm
from contactus.models import Contactus

# Create your views here.
def contactus(request: HttpRequest):
    myForm = ContactusForm()

    if request.method == 'POST':
        myForm = ContactusForm(request.POST)
        if myForm.is_valid():
            name = myForm.cleaned_data['name']
            email = myForm.cleaned_data['email']
            message = myForm.cleaned_data['message']

            contactus = Contactus(name = name, email = email, message = message)
            contactus.save()

            notify = "Hi {}, we received your message".format(name)

            return HttpResponse(notify)

    return render(request, 'contactus/contactus.html', { 'myForm': myForm })
