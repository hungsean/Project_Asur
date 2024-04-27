import pyautogui
import time
import my_time as time_function
import screeninfo


def get_screen_info():
    monitors = screeninfo.get_monitors()
    for monitor in monitors:
        print(f"螢幕 {monitor.name} ({monitor.is_primary}): 位置 ({monitor.x}, {monitor.y}), 寬度 {monitor.width}, 高度 {monitor.height}")

get_screen_info()

# while True:
#     start_time = time.time()
#     # 獲取主螢幕的大小
#     screen_width, screen_height = pyautogui.size()

#     # 獲取目前滑鼠的位置
#     current_mouse_x, current_mouse_y = pyautogui.position()

#     print(f"螢幕尺寸：寬度={screen_width}, 高度={screen_height}")
#     print(f"目前滑鼠位置：X={current_mouse_x}, Y={current_mouse_y}")
#     time_function.reduce_frequency(start_time, 1)
