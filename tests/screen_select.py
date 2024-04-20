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

monitor_index = 0
def update_screen_info(event):
    global monitor_index
    monitor_index = screen_selector.current()
    selected_monitor = monitors[monitor_index]
    start_button.config(state="normal")
    # info_label.config(text=f"Screen {monitor_index+1}: {selected_monitor.width} x {selected_monitor.height}")


run_loop_bool = True
def run_loop(stop_event):
    global monitor_index
    # global run_loop_bool
    # run_loop_bool = True
    # global monitors
    while not stop_event.is_set():
        with mss.mss() as sct:
            sct_monitor = sct.monitors[monitor_index+1]
            screenshot = sct.grab(sct_monitor)
            screenshot_PIL = Image.frombytes('RGB', (screenshot.width, screenshot.height), screenshot.rgb)
            screenshot_np = np.array(screenshot_PIL)
            screenshot_np = screenshot_np[:, :, :3]
            # print(screenshot_np.shape)
            category_name = category_index.main(screenshot_np)
            category_label.config(text=category_name)
    print("[INFO] stop @run_loop")
    # global run_loop_thread
    # run_loop_thread.join()
    # return


# run_loop_thread = threading.Thread(target=run_loop)
stop_event = threading.Event()
def start():
    screen_selector.pack_forget()
    start_button.pack_forget()
    category_label.pack(padx=20, pady=20)
    stop_button.pack()
    global stop_event
    stop_event.clear()
    threading.Thread(target=run_loop, args=(stop_event, )).start()
    print("start!")

    return

def stop():
    print("stopping")
    # global run_loop_thread
    # global run_loop_bool
    # run_loop_bool = False
    # time.sleep(1)
    # print("run join")
    stop_event.set()
    stop_button.pack_forget()
    start_button.pack()
    return

app = tk.Tk()
app.title("Screen Selector")

# 獲取所有螢幕的資訊
monitors = get_monitors()
screen_names = [f"Screen {i+1}: {m.width}x{m.height}" for i, m in enumerate(monitors)]

# 下拉選單讓用戶選擇螢幕
screen_selector = ttk.Combobox(app, values=screen_names, state="readonly")
screen_selector.pack(pady=20, padx=20)
screen_selector.bind("<<ComboboxSelected>>", update_screen_info)

# 顯示選定螢幕的資訊


start_button = tk.Button(app, text="start", command=start, state="disabled")
start_button.pack(padx=20,pady=20)

category_label = tk.Label(app, text="Select a screen to see its resolution")
category_label.pack_forget()

stop_button = tk.Button(app, text="stop", command=stop)
stop_button.pack_forget()

if len(monitors) == 1:
    print("[ERROR] only one monitor!")
    exit()

app.geometry("300x150")
app.mainloop()
