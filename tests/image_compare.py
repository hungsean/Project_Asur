from skimage.metrics import structural_similarity as ssim
import cv2
import garbage.image_process as image_process
import time

sample = cv2.imread("assets\images\sample\sample_homepage.png")
mask = cv2.imread("assets\images\mask\mask_homepage.png", cv2.IMREAD_UNCHANGED)
input_image = cv2.imread("assets\screenshots\Screenshot_20240418-195239.png")

# 定義疊加圖片函數
def overlay_images(background_img, overlay_img_with_alpha):
    # 確保兩張圖片具有相同的寬高
    if background_img.shape[:2] != overlay_img_with_alpha.shape[:2]:
        raise ValueError("兩張圖片的尺寸必須相同。")
    
    # 分離overlay圖片的alpha通道和顏色通道
    overlay_img = overlay_img_with_alpha[:,:,:3]  # BGR顏色通道
    alpha_mask = overlay_img_with_alpha[:,:,3] / 255.0  # 正規化alpha通道

    # 背景圖片中對應的區域需要根據alpha值進行混合
    for c in range(0, 3):
        background_img[:, :, c] = (1. - alpha_mask) * background_img[:, :, c] + alpha_mask * overlay_img[:, :, c]

    return background_img

start_time = time.time()
sample = image_process.image_preprocess(sample)
input_image = image_process.image_preprocess(input_image)

# 疊加圖片
masked_sample = overlay_images(sample, mask)
masked_input = overlay_images(input_image, mask)

masked_sample = image_process.resize_image(masked_sample, image_process.RESIZE_480P_WIDTH, image_process.RESIZE_480P_HEIGHT)
masked_input = image_process.resize_image(masked_input, image_process.RESIZE_480P_WIDTH, image_process.RESIZE_480P_HEIGHT)


# cv2.imshow("sample", masked_sample)
# cv2.imshow("input", masked_input)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

mid_time = time.time()
# 計算SSIM
ssim_index = ssim(masked_input, masked_sample, channel_axis=2)

end_time = time.time()

print("ssim:", ssim_index)
print("part1: ", (mid_time - start_time))
print("part2: ", (end_time - mid_time))
