"""
A script designed to 1) resize all of the downloaded images to desired dimension (DEFAULT 64x64 pixels) and 2) rename images in folders from 1.png to n.png for ease of use in training
"""

import os
from PIL import Image
import numpy as np


#Set your own PATH 
output_path = '/Users/amalta/Desktop/projects/images/resized-art'
images_path='/Users/amalta/Desktop/projects/images/art'

IMAGE_SIZE = 128
IMAGE_CHANNELS = 3

training_data = []
for root, dirs, files in os.walk(images_path):
    for name in dirs:
        try:
            os.stat(os.path.join(output_path, name))
        except:
            os.mkdir(os.path.join(output_path, name))

    i = 0
    for f in files:
        source = os.path.join(root, f)
        arist_name = root.split("/")[-1]
        try:
            out_path = os.path.join(os.path.join(output_path, arist_name), "{}.jpg".format(i))
            image = np.asarray(Image.open(source).resize((IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS))
            if (image.shape == (IMAGE_SIZE, IMAGE_SIZE, IMAGE_CHANNELS)):
                training_data.append(image)
            # image.save(out_path)
            i+=1
        except:
            pass


training_data = np.reshape(training_data, (-1, IMAGE_SIZE, IMAGE_SIZE, IMAGE_CHANNELS))
training_data = training_data / 127.5 - 1
np.save('training_art.npy', training_data)

