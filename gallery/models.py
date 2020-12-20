from djongo import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=100)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey('Gallery', on_delete=models.CASCADE)
