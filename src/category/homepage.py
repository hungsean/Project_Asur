import cv2
# from ..image_process import *
from function import image_process, file


sample = cv2.imread("assets\category\homepage\sample_homepage.png")
sample = image_process.preprocess(sample)
coordsArray = file.read_json("assets\category\homepage\coordinate_homepage.json")
print("homepage init finish")

def check(input_image):
    # ssim_index = image_process.compare(input_image, sample, mask)
    ssim_index = image_process.compare_crop(input_image, sample, coordsArray)

    return ssim_index