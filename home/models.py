from django.db import models

# Create your models here.


def image_upload(instance, filename):
    parts = filename.split(".")
    extension = ""
    if len(parts) == 2:
        imagename, extension = parts
    else:
        # Handle the case where there are too many or too few periods in the filename
        print("Invalid filename format:", filename)
    return "Covido/%s.%s" % (instance.id, extension)






class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "Frequently Asked Questions"





TAG = (
    ("Things You Should Do", "Things You Should Do"),
    ("Things You Shouldn't Do","Things You Shouldn't Do"),
)



class Prevention(models.Model):
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=40 , choices=TAG)
    image= models.ImageField(upload_to=image_upload)


    def __str__(self):
        return self.title
    







