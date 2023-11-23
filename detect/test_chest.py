import xray_classification
import matplotlib.pyplot as plt




loaded_model = load_model("xray_model.h5")
loaded_model.summary()
loaded_model.evaluate(test_ds, return_dict=True)
#loss, accuracy = loaded_model.evaluate(test_ds, return_dict=True))



###### Test
for image, label in test_ds.take(1):
    plt.imshow(image[0] / 255.0)
    plt.title(CLASS_NAMES[label[0].numpy()])

prediction = model.predict(test_ds.take(1))[0]
scores = [1 - prediction, prediction]

for score, name in zip(scores, CLASS_NAMES):
    print("This image is %.2f percent %s" % ((100 * score), name))