from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def all_posts(request):
    blogs_objects = Blog.objects.all()

    return render(request, 'blog/index.html', { 'blogs_objects': blogs_objects })
