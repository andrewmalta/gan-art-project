
import os
from PIL import Image
import numpy as np

BAR_WIDTH = 4
IMAGE_SIZE = 128

NUM_COLS = 7
NUM_ROWS = 4

images_path = "/Users/amalta/Desktop/projects/output/allartists-firstrun/"

def extract_pictures(image_array, iter_num):
    print(image_array.shape)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            vertical_offset = BAR_WIDTH * (1 + col) + col * IMAGE_SIZE
            horizontal_offset = BAR_WIDTH * (1 + row) + row * IMAGE_SIZE
            img = Image.fromarray(image_array[horizontal_offset:horizontal_offset + IMAGE_SIZE, vertical_offset:vertical_offset + IMAGE_SIZE, :], 'RGB')
            img.save('{}-{}-{}.jpg'.format(iter_num, row, col))
 

for root, dirs, files in os.walk(images_path):
    for f in files:
        image_path = os.path.join(root, f)
        iter_num = f.split("-")[1].split(".")[0]
        extract_pictures(np.asarray(Image.open(image_path)), iter_num)

