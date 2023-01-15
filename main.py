"""
10 de enero 0:48
"""
# import numpy as np
# import pandas as pd
# import tensorflow as tf
import os

# import cv2
# import matplotlib.pyplot as plt
# from tqdm import

# os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

path = './images'
directories = os.listdir(path)
directories.sort()

print(f'Directories: {directories}')
# print(dir([]))
# print(type(files))

images_arr = []
labels_arr = []

# for i in range(len(directories)):
#     files = os.listdir(path + "/" + directories[i])
#     print(files)

for directory in directories:
    files = os.listdir(f'{path}/{directory}')
    files.sort()
    print(f'\tDirectory {directory}: {files}')
    for file in files:
        print(f'\t\t{path}/{directory}/{file}')
