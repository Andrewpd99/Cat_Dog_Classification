import os
import tensorflow as tf
import numpy as np

# Suppress TensorFlow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppresses most TensorFlow logging

# Contains the current directory path
base_dir = os.path.abspath(os.path.dirname(__file__))

# Load and prepare the image
def load_image(filename):
    # Load image
    img = tf.keras.preprocessing.image.load_img(filename, target_size=(224, 224))
    # Convert to array
    img = tf.keras.preprocessing.image.img_to_array(img)
    # Reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # Center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img

# Load an image and predict the class
def make_prediction(image):
    # Load the image
    img = load_image(image)
    # Load the model
    model = tf.keras.models.load_model(os.path.join(base_dir, 'final_model.h5'))
    # Predict the class
    result = model.predict(img)
    if np.round(result) == 1:
        print("The image is a Dog")
    else:
        print("The image is a Cat")

# Change image_file below to predict a different image
# Approximately 98% accurate
image_file = 'sample_image.jpg'
image_location = os.path.join(base_dir, image_file)

make_prediction(image_location)
