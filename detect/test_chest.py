from keras.models import load_model
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from keras.preprocessing.image import img_to_array, load_img



loaded_model = load_model("D:/Tutorials/covido/src/detect/xray_model.h5")



image_path = "/content/Viral Pneumonia-10.png"
img = load_img(image_path, target_size=(180, 180))

# Display the image
plt.imshow(img)
plt.axis('off')
plt.show()

# Load the pre-trained model
model_path = "/content/drive/MyDrive/xray/xray_model.h5"
#model_path = "/content/xray_modelxx.h5"
loaded_model = load_model(model_path)

# Preprocess the image
img_array = img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
preprocessed_image = img_array / 255.0  # Normalize pixel values to the range of 0-1

# Make a prediction
prediction = loaded_model.predict(preprocessed_image)

# Process the prediction
predicted_class_index = np.argmax(prediction)
class_labels = ['Normal', 'Pneumonia']  # Replace with your actual class labels
predicted_label = class_labels[predicted_class_index]

#print("Predicted class:", predicted_label)

scores = [1 - prediction, prediction]

for score, name in zip(scores, class_labels):
    print("This image is %.2f percent %s" % ((100 * score), name))