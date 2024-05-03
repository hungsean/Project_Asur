import pynput
from screeninfo import get_monitors
import time
import random
from category import index as category_index
from function import frame as frame_function

SCALE_720P = (1280, 720)

monitors = get_monitors()
mouse = pynput.mouse.Controller()

SCALE_720P = (1280, 720)

def click_button(monitor_info, start_pos, end_pos, scale = SCALE_720P, sleep_time = (0.5, 2)):
    start_pos_monitor = [
        monitor_info.x + (start_pos[0] * monitor_info.width / scale[0]),
        monitor_info.y + (start_pos[1] * monitor_info.height / scale[1])
    ]
    end_pos_monitor = [
        monitor_info.x + (end_pos[0] * monitor_info.width / scale[0]),
        monitor_info.y + (end_pos[1] * monitor_info.height / scale[1])
    ]
    click_pos = random_click_pos(start_pos_monitor, end_pos_monitor)
    global mouse
    time.sleep(random.uniform(sleep_time[0], sleep_time[1]))
    mouse.position = (click_pos[0], click_pos[1])
    mouse.click(pynput.mouse.Button.left)

def random_click_pos(start_pos, end_pos, cut_scale = 0.3):
    cut_start_pos = [
        start_pos[0] + (end_pos[0] - start_pos[0]) * cut_scale,
        start_pos[1] + (end_pos[1] - start_pos[1]) * cut_scale
    ]
    cut_end_pos = [
        end_pos[0] - (end_pos[0] - start_pos[0]) * cut_scale,
        end_pos[1] - (end_pos[1] - start_pos[1]) * cut_scale
    ]
    print(int(cut_start_pos[0]), int(cut_start_pos[0]))

    result_pos = [
        random.randint(int(cut_start_pos[0]), int(cut_end_pos[0])),
        random.randint(int(cut_start_pos[1]), int(cut_end_pos[1]))
    ]
    # frame_function.create_transparent_window(result_pos, result_pos)
    return result_pos

def check_multiple(target_names: list[str], max_times: int = 5, times: int = 2, intervals: float = 0.5):
    count = 0
    for _ in range(max_times):
        now_state = category_index.check_main(target_names)
        if now_state['name'] != 'unknown':
            count += 1
        if count == times:
            return True
        time.sleep(intervals)
    return False
