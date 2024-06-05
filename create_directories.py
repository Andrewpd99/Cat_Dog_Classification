import os
from os import makedirs
from os import listdir
from shutil import copyfile
from random import seed
from random import random

# gets the current file_path and creates the dataset folder
script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_home = os.path.join(script_dir, 'dataset_dogs_vs_cats/')

# creates the sub directories and label directories within the dataset folder
subdirs = ['train/', 'test/']
for subdir in subdirs:
    labeldirs = ['dogs/', 'cats/']
    for labldir in labeldirs:
        newdir = os.path.join(dataset_home, subdir, labldir)
        makedirs(newdir, exist_ok=True)

# random seed generator
seed(1)
# ratio of pictures for validation
val_ratio = 0.25

# copy train dataset into corresponding subdirectories
src_directory = os.path.join(script_dir, 'train')
for file in listdir(src_directory):
    src = src_directory + '/' + file
    dst_dir = 'train/'
    if random() < val_ratio:
        dst_dir = 'test/'
    if file.startswith('cat'):
        dst = dataset_home + dst_dir + 'cats/' + file
        copyfile(src, dst)
    elif file.startswith('dog'):
        dst = dataset_home + dst_dir + 'dogs/' + file
        copyfile(src, dst)
    