import cv2
from function import image_process, file


sample = cv2.imread("assets\category\\retired\sample_retired.png")
sample = image_process.preprocess(sample)
coordsArray = file.read_json("assets\category\\retired\coordinate_retired.json")
print("retired init finish")

def check(input_image):
    # ssim_index = image_process.compare(input_image, sample, mask)
    ssim_index = image_process.compare_crop(input_image, sample, coordsArray)

    # debug
    # debug_index = []
    # for i in range(len(ssim_index)):
    #     debug_index.append({"index": ssim_index[i], "count":coordsArray[i]["count"]})
    # ssim_index = debug_index
    
    return ssim_index