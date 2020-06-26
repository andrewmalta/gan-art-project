import imageio
from PIL import Image
import os


def create_individual_gifs():
    images_path = "/Users/amalta/Desktop/projects/images/individual_images/"
    output_path = "/Users/amalta/Desktop/projects/images/gifs/"
    images = []
    cols = 4
    rows = 7


    for col in range(cols):
        for row in range(rows):
            print("creating gif of {} {}".format(col, row))
            iteration = 1
            images = []
            while True:
                try:
                    image_path = os.path.join(images_path, "{}-{}-{}.jpg".format(iteration, col, row))
                    image = imageio.imread(image_path)
                    images.append(image)
                    iteration += 1
                except:
                    break
            imageio.mimsave(os.path.join(output_path, "{}-{}.gif".format(col, row)), images)



def create_grid_gif():
    images_path = "/Users/amalta/Desktop/projects/output/allartists-firstrun/"
    output_path = "/Users/amalta/Desktop/projects/images/gifs/"
    images = []
    for iteration in range(1, 1001):
        try:
            image_path = os.path.join(images_path, "trained-{}.png".format(iteration))
        except:
            break
        image = imageio.imread(image_path)
        images.append(image)
        iteration += 1

    imageio.mimsave(os.path.join(output_path, "allartists-firstrun.gif"), images)


if __name__ == "__main__":
    create_grid_gif()