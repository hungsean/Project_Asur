import cv2
from image_process import *
from skimage.metrics import structural_similarity as ssim

HOME_PAGE_SAMPLE = cv2.imread('data\img\sample\sample_homepage.png', cv2.IMREAD_GRAYSCALE)
def check_homepage(input_image):
    cropped_input_image = crop_bottom_percent(input_image, 8.75)
    canny_input_image = canny_edges(cropped_input_image)
    # cv2.imwrite('sample_output.png', canny_input_image)
    # debug ---
    print("canny: ", canny_input_image.shape)
    print("sample: ", HOME_PAGE_SAMPLE.shape)
    # debug ---

    ssim_index = ssim(canny_input_image, HOME_PAGE_SAMPLE)
    return ssim_index