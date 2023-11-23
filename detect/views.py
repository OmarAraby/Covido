from django.shortcuts import render,redirect
from contact.models import Feedback,ImageSlide
from django.core.files.storage import FileSystemStorage  
from django.conf import settings
import os







def detect(request):

    feedbacks = Feedback.objects.all()  
    images = ImageSlide.objects.all()  
    if request.method == 'POST':
        uploaded_image = request.FILES['image']
       

        # Save the uploaded image to a temporary location
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        #Dvalue=XrayPreduction.XrayP(str(filename))

        # Construct the URL to the uploaded image
        result_url = fs.url(filename)

        # Redirect to 'detect:result_chest' with the image URL as a parameter
        return  render(request, 'result_chest.html', {'result_url': result_url,'feedbacks': feedbacks, 'images': images})

    # If the request method is not POST, render the form
    return render(request, 'detect.html')


def result_chest(request):
    feedbacks = Feedback.objects.all()  
    images = ImageSlide.objects.all()  
    #result_url = request.GET.get('result', None)

    context = {'feedbacks': feedbacks, 'images': images}

    return render(request, 'result_chest.html', context)


















#import tensorflow as tf
#from tensorflow.python import keras
# import numpy as np
# from keras_preprocessing.image import ImageDataGenerator


# # Create your views here.


# # Load the model
# # Load your model
#model = keras.models.load_model('xray_model.h5')

# target_size = (224, 224)

# def process_uploaded_image(uploaded_image):
#    # Convert the uploaded image to a format compatible with model prediction
#     img = ImageDataGenerator.load_img(uploaded_image, target_size=target_size)
#     img_array = ImageDataGenerator.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0  # Normalize pixel values

#     # Make predictions
#     result = model.predict(img_array)

#     # You may need to post-process the result based on your specific model and task

#     return result

