from . import homepage
from . import retired
from . import dock_full
from function import image_process
import time



def main(main_input_image):
    main_input_image = image_process.preprocess(main_input_image)
    response = ""
    start_time = time.time()

    # homepage
    homepage_index = homepage.check(main_input_image)
    homepage_index = avg(homepage_index)
    response += f"homepage: {homepage_index:.2f}\n"

    # retired
    retired_index = retired.check(main_input_image)
    retired_index = avg(retired_index)
    response += f"retired: {retired_index:.2f}\n"
    
    # dock_full
    dock_full_index = dock_full.check(main_input_image)
    dock_full_index = avg(dock_full_index)
    response += f"dock_full: {dock_full_index:.2f}\n"

    # debug
    # response += "dock_full ----\n"
    # for dock_full_entry in dock_full_index:
    #     response += f"{dock_full_entry['count']} : {dock_full_entry['index']:.2f}\n"

    end_time = time.time()
    print("[INFO] time: ", f"{(end_time - start_time):.3}")
    return response

def avg(array):
    if not array:  # 檢查列表是否為空
        return 0  # 如果列表為空，返回0或其他合適的值
    return sum(array) / len(array)