import tkinter as tk
import threading
import time

from frame import mode_selector, start as start_frame
from function import frame as frame_function, image_process as image_function
from category import index as category_index


frame = None
text_label = None
start_button = None
back_button = None

def init_frame(import_app):
    global frame
    if frame is None:
        frame = tk.Frame(import_app)

        # init widgets
        global text_label
        text_label = tk.Label(frame, text="change to start screen\nand press start")
        text_label.pack()
        global start_button
        start_button = tk.Button(frame, text="Start", command=start)
        start_button.pack(side=tk.LEFT, padx=10)
        global back_button
        back_button = tk.Button(frame, text="back", command=back_button_active)
        back_button.pack(side=tk.LEFT, padx=10)

def back_button_active():
    frame_function.swap_frame(frame, mode_selector.frame)
    return



stop_event = threading.Event()
def start():
    start_button.config(state="disabled")
    check_result_max = category_index.check_main(['start_sorties'])
    if check_result_max['name'] == "unknown":
        global text_label
        text_label.config(text=f"Please\n{text_label.cget('text')}")
        start_button.config(state='normal')
        return
    
    return

def stop():
    global is_pause
    print("stopping")
    stop_event.set()
    is_pause = True
    return