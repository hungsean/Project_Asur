import pynput
import random
from screeninfo import get_monitors
import time

monitors = get_monitors()
mouse = pynput.mouse.Controller()

SCALE_720P = (1280, 720)

def click_button(monitor_info, start_pos, end_pos, scale = SCALE_720P, sleep_time = (1, 3)):
    start_pos_monitor = [
        monitor_info.x + start_pos[0] * monitor_info.width / scale[0],
        monitor_info.y + start_pos[1] * monitor_info.height / scale[1]
    ]
    end_pos_monitor = [
        monitor_info.x + end_pos[0] * monitor_info.width / scale[0],
        monitor_info.y + end_pos[1] * monitor_info.height / scale[1]
    ]
    click_pos = random_click_pos(start_pos_monitor, end_pos_monitor)
    global mouse
    mouse.position = (click_pos[0], click_pos[1])
    time.sleep(random.uniform(sleep_time[0], sleep_time[1]))
    mouse.click(pynput.mouse.Button.left)

def random_click_pos(start_pos, end_pos, cut_scale = 0.2):
    cut_start_pos = [
    start_pos[0] + (end_pos[0] - start_pos[0]) * cut_scale,
    start_pos[1] + (end_pos[1] - start_pos[1]) * cut_scale
    ]
    cut_end_pos = [
        end_pos[0] - (end_pos[0] - start_pos[0]) * cut_scale,
        end_pos[1] - (end_pos[1] - start_pos[1]) * cut_scale
    ]

    print("start: ",cut_start_pos)
    print("end: ",cut_end_pos)
    result_pos = [
        random.randint(int(start_pos[0]), int(end_pos[0])),
        random.randint(int(start_pos[1]), int(end_pos[1]))
    ]
    return result_pos

click_button(monitors[0], [0,0], [100, 100])

    

