"""
10 de enero 0:48
"""
import numpy as np
import pandas as pd
# import tensorflow as tf
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
