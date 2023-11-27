from django.shortcuts import render,redirect
from contact.models import Feedback,ImageSlide
from .models import UploadedImage
from django.urls import reverse
from django.core.files.storage import FileSystemStorage  
from django.conf import settings
from tensorflow.python import keras
from keras.preprocessing.image import img_to_array,load_img
import numpy as np
from keras.models import load_model
import io

# from PIL import Image

# def load_img(image_path, target_size):
#     return Image.open(image_path).resize(target_size)




# from keras.layers import BatchNormalization ,Rescaling
# custom_objects = {'BatchNormalization': BatchNormalization, 'Rescaling': Rescaling}




model  = load_model('D:/Tutorials/covido/src/detect/xray_modelxx.h5')



def detect(request):
    feedbacks = Feedback.objects.all()  
    images = ImageSlide.objects.all()  

    if request.method == 'POST':
        uploaded_image = request.FILES['image']

        
        # Create an instance of UploadedImage and save it to the database
        uploaded_image_instance = UploadedImage.objects.create(image=uploaded_image)
        print('Image NAme :',uploaded_image_instance.image.name)
      

        img = load_img(uploaded_image_instance.image.path, target_size=(180, 180))
        
        # # Preprocess the image
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        preprocessed_image = img_array / 255.0  # Normalize pixel values to the range of 0-1


        # # Make a prediction
        prediction = model.predict(preprocessed_image)

        # # Process the prediction
        predicted_class_index = np.argmax(prediction)
        class_labels = ['Normal', 'Pneumonia']  # Replace with your actual class labels
        predicted_label = class_labels[predicted_class_index]


        scores = [100 * (1 - prediction[0][0]), 100 * prediction[0][0]]

        combined_data = list(zip(scores, class_labels))
        for score, name in combined_data:
            print("This image is %.2f percent %s" % ((score), name))


        context = {
            'uploaded_image': uploaded_image_instance,
            'feedbacks': feedbacks,
            'images': images,
            'combined_data':combined_data,
        }

        # Redirect to 'detect:result_chest' with the image URL as a parameter
        return  render(request, 'result_chest.html', context)

    # If the request method is not POST, render the form
    return render(request, 'detect.html')























# def result_chest(request):
#     feedbacks = Feedback.objects.all()  
#     images = ImageSlide.objects.all()  
#     #result_url = request.GET.get('result', None)

#     context = {'feedbacks': feedbacks, 'images': images}

#     return render(request, 'result_chest.html', context)















