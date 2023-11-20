from django.db import models
from home.models import image_upload
# Create your models here.


class Info(models.Model):
    place = models.CharField(max_length=50)
    phone_number = models.CharField( max_length=20)
    email = models.EmailField( max_length=254)
 
    

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.email





class Feedback(models.Model):
    name = models.CharField(max_length=25)
    feedback = models.TextField(max_length=1000)
    image= models.ImageField(upload_to=image_upload)


    def __str__(self):
        return self.name
    



class ImageSlide(models.Model):
    name = models.CharField(max_length=25)
    image= models.ImageField(upload_to=image_upload)


    def __str__(self):
        return self.name
    

