"""
10 de enero 0:48
"""
import numpy as np
import pandas as pd
import tensorflow as tf
import os
# import cv2
# import matplotlib.pyplot as plt
# from tqdm import

# os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

path = './images'
files = os.listdir(path)
files.sort()

print(files)
print(dir([]))
print(type(files))
