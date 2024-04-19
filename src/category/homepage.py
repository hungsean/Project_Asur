import cv2
# from ..image_process import *
from function import image_process

from skimage.metrics import structural_similarity as ssim

# HOME_PAGE_SAMPLE = cv2.imread('assets\images\sample\sample_homepage.png', cv2.IMREAD_GRAYSCALE)
def check_homepage(input_image):
    sample = cv2.imread('assets\images\sample\sample_homepage.png', cv2.IMREAD_GRAYSCALE)
    sample = image_process.crop_bottom_percent(sample, 8.75)
    input_image = image_process.crop_bottom_percent(input_image, 8.75)
    sample = image_process.canny_edges(sample)
    input_image = image_process.canny_edges(input_image)
    # canny_input_image = image_process.canny_edges(cropped_input_image)
    # cv2.imwrite('sample_output.png', canny_input_image)
    # debug ---
    # print("canny: ", canny_input_image.shape)
    # print("sample: ", HOME_PAGE_SAMPLE.shape)
    # debug ---

    # cv2.imshow("input", input_image)
    # cv2.imshow("sample", sample)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    ssim_index = ssim(input_image, sample)
    return ssim_index