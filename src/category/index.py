# from . import homepage
# from . import retired
# from . import dock_full

import time
import cv2
import importlib
import winsound

from function import image_process, file
from frame import start as start_frame

category_path = file.find_subdirectories("assets\category")
# [{"name": <name>, "path": <path>}]
category_assets = []
for category_entry in category_path:
    name = category_entry["name"]
    path = category_entry["path"]
    sample = cv2.imread(path + "\sample.png")
    sample = image_process.preprocess(sample)
    coordsArray = file.read_json(path + "\coordinate.json")
    # execute = importlib.import_module(f"category.{name}").execute
    category_assets.append({"name": name, "sample": sample, "coordsArray": coordsArray})
# [{"name": <name>, "sample": <sample>, "coordsArray": <coordsArray>}]


category_result_end = {}
def debug(main_input_image, target: str):
    main_input_image = image_process.preprocess(main_input_image)
    response = ""
    start_time = time.time()

    category_result = []

    for category_entry in category_assets:
        name = category_entry["name"]
        sample = category_entry["sample"]
        coordsArray = category_entry["coordsArray"]
        ssim_index = image_process.compare_crop(main_input_image, sample, coordsArray)
        ssim_index_avg = avg(ssim_index)
        category_result.append({"name": name, "index": ssim_index_avg})
        response += f"{name}: {ssim_index_avg:.2f}\n"

    global category_result_end
    category_result_end_temp = max(category_result, key=lambda x: x['index'])
    if category_result_end_temp['index'] < 0.5:
        category_result_end_temp['name'] = "unknown"
    category_result_end = category_result_end_temp
    response += f"\n{category_result_end['name']}: {category_result_end['index']:.2f}\n"

    # debug
    debug_category = find_name(category_assets, target)
    debug_name = debug_category["name"]
    debug_sample = debug_category["sample"]
    debug_coordsArray = debug_category["coordsArray"]
    debug_ssim_index = image_process.compare_crop(main_input_image, debug_sample, debug_coordsArray)
    debug_index = []
    for i in range(len(debug_ssim_index)):
        debug_index.append({"index": debug_ssim_index[i], "count":debug_coordsArray[i]["count"]})   
    response += f"{debug_name} ----\n"
    for debug_entry in debug_index:
        response += f"{debug_entry['count']} : {debug_entry['index']:.2f}\n"

    

    end_time = time.time()
    print("[INFO] time: ", f"{(end_time - start_time):.2f}")
    return response

def check_sub(input_image, target_names: list[str]):
    input_image = image_process.preprocess(input_image)
    global category_assets
    target_list = filter_dicts(target_names, category_assets)
    result_list = []
    for target_entry in target_list:
        target_index = image_process.compare_crop(input_image, target_entry['sample'], target_entry['coordsArray'])
        target_index_avg = avg(target_index)
        result_list.append({"name": target_entry['name'], "index": target_index_avg})
        
    return result_list

def check_main(target_names: list[str]):
    now_screenshot = image_process.screenshot(start_frame.monitor_index)
    check_result = check_sub(now_screenshot, target_names)
    check_result_max = data_post_process(check_result)
    return check_result_max

def avg(array):
    if not array:  # 檢查列表是否為空
        return 0  # 如果列表為空，返回0或其他合適的值
    return sum(array) / len(array)

def find_name(array, name):
    for entry in array:
        if entry["name"] == name:
            return entry
    return None

def get_category_end():
    return category_result_end["name"]

def filter_dicts(names, dict_list):
    # 將 names 轉換為集合以提高查找效率
    name_set = set(names)
    # 初始化輸出陣列
    output_dicts = []
    # 遍歷 dict_list，檢查每個字典的 "name" 是否存在於 name_set 中
    for item in dict_list:
        if item['name'] in name_set:
            output_dicts.append(item)
    if len(output_dicts) != len(names):
        print("[ERROR] have name not exist @category/index.py.filter_dicts")
        return None
    return output_dicts

def data_post_process(result_list):
    result_max = max(result_list, key=lambda x: x['index'])
    if result_max['index'] < 0.5:
        result_max['name'] = "unknown"
    return result_max
