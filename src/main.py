import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors
import threading
import mss
from PIL import Image
import cv2
import numpy as np
import time

from category import index as category_index
from frame import start as start_frame
from frame import mode_selector as mode_selector_frame
from frame import debug_mode as debug_mode_frame

# monitor_index = 0
# def update_screen_info(event):
#     global monitor_index
#     monitor_index = screen_selector.current()
#     selected_monitor = monitors[monitor_index]
#     start_button.config(state="normal")
#     # info_label.config(text=f"Screen {monitor_index+1}: {selected_monitor.width} x {selected_monitor.height}")

# # 設定迴圈的執行頻率，每秒執行一次
# frequency = 1.0  # 頻率（Hz），這裡是每秒
# period = 1.0 / frequency  # 每次迴圈的時間間隔，單位是秒
# run_loop_bool = True
# def run_loop(stop_event):
#     global monitor_index
#     # global run_loop_bool
#     # run_loop_bool = True
#     # global monitors
#     last_time = time.time()
#     while not stop_event.is_set():
#         start_time = time.time()  # 紀錄迴圈開始時間
#         with mss.mss() as sct:
#             sct_monitor = sct.monitors[monitor_index+1]
#             screenshot = sct.grab(sct_monitor)
#             screenshot_PIL = Image.frombytes('RGB', (screenshot.width, screenshot.height), screenshot.rgb)
#             screenshot_np = np.array(screenshot_PIL)
#             screenshot_np = screenshot_np[:, :, :3]
#             # print(screenshot_np.shape)
#             category_name = category_index.main(screenshot_np)
#             print("result: ",category_index.get_category_end())
#             category_label.config(text=category_name)
#         elapsed_time = time.time() - start_time  # 計算迴圈執行所花費的時間
#         sleep_time = period - elapsed_time  # 計算需要等待的時間
#         if sleep_time > 0:
#             time.sleep(sleep_time)  # 等待一定時間，以保持固定的頻率執行
#     print("[INFO] stop @run_loop")
#     # global run_loop_thread
#     # run_loop_thread.join()
#     # return


# # run_loop_thread = threading.Thread(target=run_loop)
# stop_event = threading.Event()
# def start():
#     screen_selector.pack_forget()
#     start_button.pack_forget()
#     category_label.pack(padx=20, pady=20)
#     stop_button.pack()
#     global stop_event
#     stop_event.clear()
#     threading.Thread(target=run_loop, args=(stop_event, )).start()
#     print("start!")

#     return

# def stop():
#     print("stopping")
#     # global run_loop_thread
#     # global run_loop_bool
#     # run_loop_bool = False
#     # time.sleep(1)
#     # print("run join")
#     stop_event.set()
#     stop_button.pack_forget()
#     start_button.pack()
#     return

# def debug_mode_pause():

# def debug_mode_active():
#     # TODO
#     return 

app = tk.Tk()
app.title("Screen Selector")

start_frame.init_frame(app)
mode_selector_frame.init_frame(app)
debug_mode_frame.init_frame(app)
start_frame.frame.pack()






# get monitors information
# monitors = get_monitors()
# screen_names = [f"Screen {i+1}: {m.width}x{m.height}" for i, m in enumerate(monitors)]

# # ---
# # init start_frame
# start_frame = tk.Frame(app)
# # create selector
# screen_selector = ttk.Combobox(start_frame, values=screen_names, state="readonly")
# screen_selector.pack(pady=20, padx=20)
# screen_selector.bind("<<ComboboxSelected>>", update_screen_info)
# # create button
# start_button = tk.Button(start_frame, text="start", command=start, state="disabled")
# start_button.pack(padx=20,pady=20)
# # show start_frame
# start_frame.pack(fill="both", expand=True)
# # ---

# # ---
# # init select_frame
# select_frame = tk.Frame(app)
# # create button
# debug_mode_button = tk.Button(select_frame, text="debug mode", command=debug_mode_active)
# # ---

# # ---
# # init debug_mode_frame
# debug_mode_frame = tk.Frame(app)
# # create label
# category_label = tk.Label(app, text="Null")
# category_label.pack(padx=20, pady=20)
# # create pause button
# pause_button = tk.Button(debug_mode_frame, text="pause", command=pause)

# stop_button = tk.Button(app, text="stop", command=stop)
# stop_button.pack_forget()

if start_frame.isSingleScreen():
    print("[ERROR] only one monitor!")
    exit()

app.geometry("300x150")
app.mainloop()
