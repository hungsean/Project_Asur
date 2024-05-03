import tkinter as tk
import time
import threading

from frame import mode_selector, start as start_frame
from function import frame as frame_function
from function import image_process as image_function
from function import time as time_function
from category import index as category_index

frame = None
text_label = None
pause_button = None
back_button = None

def init_frame(import_app):
    global frame
    if frame is None:
        frame = tk.Frame(import_app)

        # init widgets
        global text_label
        text_label = tk.Label(frame, text="Null")
        text_label.pack()
        global pause_button
        pause_button = tk.Button(frame, text = "pause", command=pause_button_active)
        pause_button.pack(side=tk.LEFT)
        global back_button
        back_button = tk.Button(frame, text = "back", command=back_button_active)
        back_button.pack(side=tk.RIGHT)

is_pause = False
def pause_button_active():
    global is_pause
    if is_pause == False:
        stop()
        
    else:
        start()
        
    return

def back_button_active():
    stop()
    frame_function.swap_frame(frame, mode_selector.frame)
    
    return

def run_loop(stop_event):
    while not stop_event.is_set():
        start_time = time.time()  # 紀錄迴圈開始時間
        screenshot = image_function.screenshot(start_frame.monitor_index)
        category_name = category_index.debug(screenshot, "sub_chapter_stopping")   
        print("result: ",category_index.get_category_end())
        text_label.config(text=category_name)
        time_function.reduce_frequency(start_time, 1)
    print("[INFO] stop @run_loop")
    # global run_loop_thread
    # run_loop_thread.join()
    # return


# run_loop_thread = threading.Thread(target=run_loop)
stop_event = threading.Event()
def start():
    global stop_event, is_pause
    stop_event.clear()
    threading.Thread(target=run_loop, args=(stop_event, )).start()
    print("start!")
    pause_button.config(text="pause")
    is_pause = False
    return

def stop():
    global is_pause
    print("stopping")
    stop_event.set()
    pause_button.config(text="start")
    is_pause = True
    return
    