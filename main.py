"""
10 de enero 0:48
"""
import numpy as np
import pandas as pd
import tensorflow as tf
import os

import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm

# os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

path = './images'
directories = os.listdir(path)
directories.sort()

# print(f'Directories: {directories}')
# print(dir([]))
# print(type(files))

images = []
labels = []

# for i in range(len(directories)):
#     files = os.listdir(path + "/" + directories[i])
#     print(files)

for directory in tqdm(directories):
    files = os.listdir(f'{path}/{directory}')
    files.sort()
    # print(f'\tDirectory {directory}: {files}')
    for index, file in enumerate(files):
        # print(f'\t\t{path}/{directory}/{file}')
        image = cv2.imread(f'{path}/{directory}/{file}')
        image = cv2.resize(image, (96, 96))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        images.append(image)
        labels.append(index)
        # print(image, index)
        # cv2.imshow(file, image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

images = np.array(images)
labels = np.array(labels, dtype=float)

print(labels)

# from sklearn.model_selection import train_test_split

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(images, labels, test_size=0.15)

# X_train 85% of images
# X_test 15% of images

# Create a model
from keras import layers, callbacks, utils, applications, optimizers
from keras.models import Sequential, Model, load_model

model = Sequential()
# add pretrained models to Sequential model
# EfficientNetB0 pretrained model
pretrained = tf.keras.applications.EfficientNetB0(input_shape=(96, 96, 3), include_top=False)
model.add(pretrained)

# add Pooling to model
model.add(layers.GlobalAvgPool2D())

# add dropout to model accuracy by reducer overwriting
model.add(layers.Dropout(0.3))

# add dese layer to as in output
model.add(layers.Dense(1))

# build model
model.build(input_shape=(None, 96, 96, 3))

# to see model summary
model.summary()
