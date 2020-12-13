from django.shortcuts import render
from gallery.models import Gallery

# Create your views here.
def gallery_list(request):
    gallery_objects = Gallery.objects.all()

    return render(request, 'gallery/gallery.html', { 'gallery_objects': gallery_objects })

def gallery_detail(request, id):
    gallery_item = Gallery.objects.get(id = id)

    return render(request, 'gallery/detail.html', { 'gallery_item': gallery_item })
