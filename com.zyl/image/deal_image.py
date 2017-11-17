
from PIL import Image
import numpy as np


def loadImage():
    im = Image.open("../../data/cat/1.jpeg")

    im.show()

    im = im.convert("RGB")
    im.show()
    # data = im.getdata()
    data = np.array(im)
    #     print data
    # print data.shape
    # data = np.resize(data, (512, 512))
    # new_im = Image.fromarray(data)
    #
    # new_im.show()
    # data.shape=(256,256,256)
    for i in range(3,235):
        data[:][:][i] = 0
    print data.shape
    print data.dtype
    print data.size
    print type(data)

loadImage()