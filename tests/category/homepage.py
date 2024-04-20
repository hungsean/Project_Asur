import cv2
# from ..image_process import *
from function import image_process
import json


sample = cv2.imread("assets\category\homepage\sample_homepage.png")
sample = image_process.preprocess(sample)
# mask = cv2.imread("assets\images\mask\mask_homepage.png", cv2.IMREAD_UNCHANGED)
# mask = image_process.preprocess(mask)
try:
    with open('assets\category\homepage\coordinate_homepage.json', 'r', encoding='utf-8') as file:
        coordsArray = json.load(file)
except FileNotFoundError:
    print("未找到原始文件 'rectangles.json'。請確認文件是否存在。")
except json.JSONDecodeError:
    print("原始文件 'rectangles.json' 格式錯誤。")

print("homepage init finish")

# HOME_PAGE_SAMPLE = cv2.imread('assets\images\sample\sample_homepage.png', cv2.IMREAD_GRAYSCALE)
def check(input_image):
    # ssim_index = image_process.compare(input_image, sample, mask)
    ssim_index = image_process.compare_crop(input_image, sample, coordsArray)
    
    return ssim_index