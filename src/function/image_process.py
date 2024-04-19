import os
import cv2

def get_png_paths(folder_path):
    png_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.png'):
                png_paths.append(os.path.join(root, file))
    return png_paths

def get_png_image(folder_path):
    
    # 讀取圖片路徑
    image_paths = get_png_paths(folder_path)

    # 讀取圖片並放入images
    images = []
    for image_path in image_paths:
        image_temp = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        images.append(image_temp)

    return images

ASPECT_16_9 = 1.7778
def image_check_aspect(input_image, input_aspect = ASPECT_16_9, tolerance=0.02):
    input_image = fix_input_image(input_image)

    # 獲取高度和寬度
    input_image_height, input_image_width = input_image.shape
    
    # 計算長寬比
    input_image_aspect = input_image_width / input_image_height
    
    # 檢查是否在容許的誤差範圍內
    if input_image_aspect < (input_aspect + tolerance) and input_image_aspect > (input_aspect - tolerance):
        # 在此範圍內return true
        return True
    else:
        # 不再此範圍內return false
        return False
    
RESIZE_1080P_HEIGHT = 1080
RESIZE_1080P_WIDTH = 1920

def resize_image(input_image, target_width = RESIZE_1080P_WIDTH, target_height = RESIZE_1080P_HEIGHT):
    # 縮放圖片至指定的長寬
    resized_image = cv2.resize(input_image, (target_width, target_height))
    return resized_image

# 裁切
def crop_bottom_percent(input_image, percent):
    input_image = fix_input_image(input_image)
    
    # 获取图像高度和宽度

    height, width= input_image.shape
    
    # 计算要裁剪的像素数
    crop_height = int(height * (1 - (percent / 100)))
    
    # 裁剪图像
    cropped_image = input_image[crop_height: , : ]
    
    return cropped_image

def canny_edges(input_image):
    # 使用Canny邊緣檢測突出邊緣
    processed_canny_edges = cv2.Canny(input_image, 150, 200)
    return processed_canny_edges

def image_preprocess(input_image):
    if (image_check_aspect(input_image) == False):
        print("[ERROR] wrong aspect")
        return None
    resized_image = resize_image(input_image)
    return resized_image

def compare(settings, sample, reference):
    

def fix_input_image(input_image):
    if len(input_image.shape) == 3:
        input_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)
    return input_image