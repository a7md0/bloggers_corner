from django.http.request import HttpRequest
from django.shortcuts import render
from gallery.models import Gallery, Comment
from gallery.forms import CommentForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def gallery_list(request):
    gallery_objects = Gallery.objects.all()

    return render(request, 'gallery/gallery.html', { 'gallery_objects': gallery_objects })

@login_required
def gallery_detail(request: HttpRequest, id):
    gallery_item = Gallery.objects.get(id = id)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # author = form.cleaned_data['author']
            author = request.user.username
            body = form.cleaned_data['body']

            comment = Comment(author = author, body = body, item = gallery_item)
            comment.save()
    
    comments = Comment.objects.filter(item=id)

    return render(request, 'gallery/detail.html', { 'gallery_item': gallery_item, 'comments': comments, 'form': form })
