import os
from os import makedirs
from os import listdir
from shutil import copyfile


# gets the current file_path and creates the dataset folder
script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_home = os.path.join(script_dir, 'finalize_dogs_vs_cats/')

# creates the label directories within the dataset folder
labeldirs = ['dogs/', 'cats/']
for labldir in labeldirs:
    newdir = os.path.join(dataset_home, labldir)
    makedirs(newdir, exist_ok=True)

# copy train dataset into corresponding subdirectories
src_directory = os.path.join(script_dir, 'train')
for file in listdir(src_directory):
    src = src_directory + '/' + file
    if file.startswith('cat'):
        dst = dataset_home + 'cats/' + file
        copyfile(src, dst)
    elif file.startswith('dog'):
        dst = dataset_home + 'dogs/' + file
        copyfile(src, dst)
    