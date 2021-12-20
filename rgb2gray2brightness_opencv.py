import cv2
import numpy as np

def rgb2gray2brightness(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    cols, rows = img.shape
    brightness = np.sum(img) / (255 * cols * rows)
    return brightness * 100    # [%]