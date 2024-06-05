import os
from os import listdir
from numpy import asarray
from numpy import save
from keras.utils import load_img, img_to_array
#from keras.preprocessing.image import load_img
#from keras.preprocessing.image import img_to_array

# gathers current os path as directory, along with training folder
script_dir = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(script_dir, 'train')

# resizes images in the train folder for 200x200 pixels. Cats get 0 value and Dogs get 1 values.
photos, labels = list(), list()
for file in listdir(folder):
    output = 0.0
    if file.startswith('dog'):
        output = 1.0
    photo = load_img(os.path.join(folder, file), target_size =(200, 200))
    photo = img_to_array(photo)
    photos.append(photo)
    labels.append(output)

# reflects all changes in photos and labels array
photos = asarray(photos)
labels = asarray(labels)
print(photos.shape, labels.shape)

# saves photos
save('dogs_vs_cats_photos.npy', photos)
save('dogs_vs_cats_labels.npy', labels)
