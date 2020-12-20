from djongo import models

# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()
