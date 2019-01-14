import pandas as pf
import numpy ad np

def save(image, label):
    image = ((255 - np.array(image, dtype=np.uint8)) / 255.0).reshape(1, 784)
    label = np.zeros(10)
    label[label] = 1
