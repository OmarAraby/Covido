from django.db import models

# Create your models here.
def image_xray_upload(instance, filename):
    parts = filename.split(".")
    extension = ""
    if len(parts) == 2:
        imagename, extension = parts
    else:
        # Handle the case where there are too many or too few periods in the filename
        print("Invalid filename format:", filename)
    return "Xray_images/%s.%s" % (instance.id, extension)






class UploadedImage(models.Model):
    image = models.ImageField(upload_to=image_xray_upload)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image.name} - {self.uploaded_at}"
