from django.urls import path
from gallery import views

app_name = "gallery"
urlpatterns = [
    path('', views.gallery_list, name="gallery_list"),
    path('<int:id>', views.gallery_detail, name="gallery_detail"),
]
