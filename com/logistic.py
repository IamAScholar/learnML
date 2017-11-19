import os
from PIL import Image
import numpy as np
import math

size = (64, 64)


def deal_image(img):
    img = img.resize(size)
    img = np.array(img)
    shape = img.shape
    img = img.reshape(shape[0] * shape[1] * shape[2])
    print img.shape
    return img
def get_images(path, is_targe):
    images_tuple = []
    files = os.listdir(path)
    abs_name = path + "/%s"

    for name in files:
        img = Image.open(abs_name % name)
        img = deal_image(img)
        images_tuple.append((img, is_targe))
    return images_tuple

def basic_sigmoid(x):
    s = 1.0 / (1.0 + math.exp(-x))
    return s

def sigmoid_derivative(x):
    s = basic_sigmoid(x)
    ds =  s * (1 - s)
    return ds



if __name__ == '__main__':
    cat = get_images("../data/cat", 1)
    b = w = np.zeros(cat[0][0].shape[0])

    print w.shape, len(b)
    # print cat
