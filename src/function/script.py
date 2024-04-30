import pyautogui
import time
import random
from category import index as category_index

SCALE_720P = (1280, 720)

def click_button(monitor_info, start_pos, end_pos, scale = SCALE_720P, sleep_time = (1, 3)):
    print(f"[INFO] start pos: {start_pos}")
    print(f"[INFO] end pos: {end_pos}")
    start_pos_monitor = []
    start_pos_monitor.append(monitor_info.x + start_pos[0] * monitor_info.width / scale[0])
    start_pos_monitor.append(monitor_info.y + start_pos[1] * monitor_info.height / scale[1])
    
    end_pos_monitor = []
    end_pos_monitor.append(monitor_info.x + end_pos[0] * monitor_info.width / scale[0])
    end_pos_monitor.append(monitor_info.y + end_pos[1] * monitor_info.height / scale[1])
    print(f"[INFO] start pos monitor: {start_pos_monitor}")
    print(f"[INFO] end pos monitor: {end_pos_monitor}")
    click_pos = random_click_pos(start_pos_monitor, end_pos_monitor)
    print(f"[INFO] click pos: {click_pos}")
    pyautogui.moveTo(click_pos[0], click_pos[1])
    time.sleep(random.uniform(sleep_time[0], sleep_time[1]))
    pyautogui.click()

def random_click_pos(start_pos, end_pos, cut_scale = 0.2):
    cut_start_pos = []
    cut_start_pos.append(start_pos[0] + (end_pos[0] - start_pos[0]) * cut_scale)
    cut_start_pos.append(start_pos[1] + (end_pos[1] - start_pos[1]) * cut_scale)
    cut_end_pos = []
    cut_end_pos.append(end_pos[0] - (end_pos[0] - start_pos[0]) * cut_scale)
    cut_end_pos.append(end_pos[1] - (end_pos[1] - start_pos[1]) * cut_scale)
    result_pos = []
    result_pos.append(random.randint(int(start_pos[0]), int(end_pos[0])))
    result_pos.append(random.randint(int(start_pos[1]), int(end_pos[1])))
    return result_pos

def check_multiple(target_names: list[str], times: int, intervals: float):
    count = 0
    for i in range(times):
        now_state = category_index.check_main(target_names)
        if now_state['name'] != 'unknown':
            count += 1
        time.sleep(intervals)
    if count != times:
        return False
    return True
