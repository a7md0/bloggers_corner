from django.urls import path
from contactus import views

app_name = "contactus"
urlpatterns = [
    path('', views.contactus, name="contactus")
]
