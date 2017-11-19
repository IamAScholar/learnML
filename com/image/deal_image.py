from PIL import Image
import numpy as np


def image2vector(image):
    v = image.reshape((image.shape[0] * image.shape[1] * image.shape[2]), 1)
    return v

def load_image(path):
    image = Image.opne(path)
    
