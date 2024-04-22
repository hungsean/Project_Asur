# from . import homepage
# from . import retired
# from . import dock_full
from function import image_process, file
import time
import cv2

category_path = file.find_subdirectories("assets\category")
# [{"name": <name>, "path": <path>}]
category_assets = []
for category_entry in category_path:
    name = category_entry["name"]
    path = category_entry["path"]
    sample = cv2.imread(path + "\sample.png")
    sample = image_process.preprocess(sample)
    coordsArray = file.read_json(path + "\coordinate.json")
    category_assets.append({"name": name, "sample": sample, "coordsArray": coordsArray})
# [{"name": <name>, "sample": <sample>, "coordsArray": <coordsArray>}]


category_result_end = {}
def main(main_input_image):
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
    debug_category = find_name(category_assets, "dock_full")
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
    return category_result_end