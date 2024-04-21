# from . import homepage
# from . import retired
# from . import dock_full
from function import image_process, file
import time
import cv2

category_index = file.find_subdirectories("assets\category")
# [{"name": <name>, "path": <path>}]


def main(main_input_image):
    main_input_image = image_process.preprocess(main_input_image)
    response = ""
    start_time = time.time()

    for category_entry in category_index:
        name = category_entry["name"]
        path = category_entry["path"]
        sample = cv2.imread(path + "\sample.png")
        sample = image_process.preprocess(sample)
        coordsArray = file.read_json(path + "\coordinate.json")
        ssim_index = image_process.compare_crop(main_input_image, sample, coordsArray)
        ssim_index_avg = avg(ssim_index)
        response += f"{name}: {ssim_index_avg:.2f}\n"

    # # homepage
    # homepage_index = homepage.check(main_input_image)
    # homepage_index = avg(homepage_index)
    # response += f"homepage: {homepage_index:.2f}\n"

    # # retired
    # retired_index = retired.check(main_input_image)
    # retired_index = avg(retired_index)
    # response += f"retired: {retired_index:.2f}\n"
    
    # # dock_full
    # dock_full_index = dock_full.check(main_input_image)
    # dock_full_index = avg(dock_full_index)
    # response += f"dock_full: {dock_full_index:.2f}\n"

    # debug
    debug_category = find_name(category_index, "dock_full")
    debug_name = debug_category["name"]
    debug_path = debug_category["path"]
    print("debug: ", debug_path )
    debug_sample = cv2.imread(debug_path + "\sample.png")
    debug_sample = image_process.preprocess(debug_sample)
    debug_coordsArray = file.read_json(debug_path + "\coordinate.json")
    debug_ssim_index = image_process.compare_crop(main_input_image, debug_sample, debug_coordsArray)
    debug_index = []
    for i in range(len(debug_ssim_index)):
        debug_index.append({"index": debug_ssim_index[i], "count":debug_coordsArray[i]["count"]})   
    response += f"{debug_name} ----\n"
    for debug_entry in debug_index:
        response += f"{debug_entry['count']} : {debug_entry['index']:.2f}\n"

    end_time = time.time()
    print("[INFO] time: ", f"{(end_time - start_time):.3}")
    return response

def avg(array):
    if not array:  # 檢查列表是否為空
        return 0  # 如果列表為空，返回0或其他合適的值
    return sum(array) / len(array)

def find_name(array, name):
    for entry in array:
        if entry["name"] == name:
            return entry
    return None