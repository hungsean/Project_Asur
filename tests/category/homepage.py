import cv2
# from ..image_process import *
from function import image_process
sample = cv2.imread("assets\images\sample\sample_homepage.png")
sample = image_process.preprocess(sample)
mask = cv2.imread("assets\images\mask\mask_homepage.png", cv2.IMREAD_UNCHANGED)
mask = image_process.preprocess(mask)
print("homepage init finish")

# HOME_PAGE_SAMPLE = cv2.imread('assets\images\sample\sample_homepage.png', cv2.IMREAD_GRAYSCALE)
def check(input_image):
    ssim_index = image_process.compare(input_image, sample, mask)
    
    return ssim_index