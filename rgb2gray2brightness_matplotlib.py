import numpy as np
import matplotlib.image as img

def rgb2gray2brightness(filepath):
    image = img.imread(filepath)
    w, h = image.shape[:2]
    red = image[:, :, 0]; green = image[:, :, 1]; blue = image[:, :, 2]

    if np.all(image <= 1):  # .png
        rgb2gray = 255 * (0.2989 * red + 0.5870 * green + 0.1140 * blue)
    else:  # .jpg
        rgb2gray = 0.2989 * red + 0.5870 * green + 0.1140 * blue
    brightness = np.sum(rgb2gray) / (255 * w * h)
    return brightness * 100    # [%]