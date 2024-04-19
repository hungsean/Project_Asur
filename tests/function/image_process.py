import os
import cv2
from skimage.metrics import structural_similarity as ssim

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
        image_temp = cv2.imread(image_path)
        images.append(image_temp)

    return images

ASPECT_16_9 = (16/9)
def image_check_aspect(input_image, input_aspect = ASPECT_16_9):
    # input_image = fix_input_image(input_image)

    # 計算長寬比
    print(input_image.shape)
    input_image_aspect = input_image.shape[1] / input_image.shape[0]
    print(input_image_aspect)
    
    # 檢查是否在容許的誤差範圍內
    # if input_image_aspect < (input_aspect + tolerance) and input_image_aspect > (input_aspect - tolerance):
    if input_image_aspect == input_aspect:
        # 在此範圍內return true
        return True
    else:
        # 不再此範圍內return false
        print("[INFO] wrong aspect @image_check_aspect")
        return False
    
RESIZE_4K = (3840, 2160)

RESIZE_2K = (2048, 1080)

RESIZE_1080P = (1920, 1080)

RESIZE_720P = (1280, 720)

RESIZE_480P = (853, 480)


# def resize_image(input_image, target_width = RESIZE_1080P_WIDTH, target_height = RESIZE_1080P_HEIGHT):
#     # 縮放圖片至指定的長寬
#     resized_image = cv2.resize(input_image, (target_width, target_height))
#     return resized_image

# 裁切
# def crop_bottom_percent(input_image, percent):
#     input_image = fix_input_image(input_image)
    
#     # 获取图像高度和宽度

#     height, width= input_image.shape
    
#     # 计算要裁剪的像素数
#     crop_height = int(height * (1 - (percent / 100)))
    
#     # 裁剪图像
#     cropped_image = input_image[crop_height: , : ]
    
#     return cropped_image

# def canny_edges(input_image):
#     # 使用Canny邊緣檢測突出邊緣
#     processed_canny_edges = cv2.Canny(input_image, 150, 200)
#     return processed_canny_edges

def preprocess(input_image):
    if (image_check_aspect(input_image) == False):
        return None
    resized_image = cv2.resize(input_image, RESIZE_720P)
    return resized_image

# 定義疊加圖片函數
def overlay_images(background_img, overlay_img_with_alpha):
    # 確保兩張圖片具有相同的寬高
    if background_img.shape[:2] != overlay_img_with_alpha.shape[:2]:
        raise ValueError("兩張圖片的尺寸必須相同。")
    
    # 分離overlay圖片的alpha通道和顏色通道
    overlay_img = overlay_img_with_alpha[:,:,:3]  # BGR顏色通道
    print("alpha_mask: ",overlay_img_with_alpha.shape)
    alpha_mask = overlay_img_with_alpha[:,:,3] / 255.0  # 正規化alpha通道

    # 背景圖片中對應的區域需要根據alpha值進行混合
    for c in range(0, 3):
        background_img[:, :, c] = (1. - alpha_mask) * background_img[:, :, c] + alpha_mask * overlay_img[:, :, c]

    return background_img

def compare(reference, sample, mask):
    masked_sample = overlay_images(sample, mask)
    masked_reference = overlay_images(reference, mask)
    compare_index = ssim(masked_sample, masked_reference, channel_axis=2)
    return compare_index
    

# def fix_input_image(input_image):
#     if len(input_image.shape) == 3:
#         input_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)
#     return input_image