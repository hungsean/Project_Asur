import tkinter as tk
import threading
import time

from frame import mode_selector, start as start_frame
from function import frame as frame_function, script as script_function, time as time_function
from category import index as category_index
from script import retired as retired_script, usual as usual_script


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
        start_button = tk.Button(frame, text="Start", command=start_button_active)
        start_button.pack(side=tk.LEFT, padx=10)
        global back_button
        back_button = tk.Button(frame, text="back", command=back_button_active)
        back_button.pack(side=tk.LEFT, padx=10)

def back_button_active():
    frame_function.swap_frame(frame, mode_selector.frame)
    stop()
    return

def start_button_active():
    start_button.config(state="disabled")
    global is_pause
    if (is_pause == False):
        
        stop()
    else:
        start()
    start_button.config(state="normal")

def run_loop(stop_event):
    usual_script.start_sorties()
    print("start_sorties clicked")
    time.sleep(1)
    while not stop_event.is_set():
        start_time = time.time()
        
        check_result = category_index.check_main(['dock_full', 'start_sorties', 'total_rewards', 'total_rewards_stop', 'total_rewards_stop_1'])
        print("[info] check result: ", check_result['name'])
        if check_result['name'] == 'unknown':
            print("unknown")
        elif check_result['name'] == 'dock_full':
            retired_script.dock_full()
        elif check_result['name'] == 'total_rewards':
            usual_script.total_rewards()
        elif check_result['name'] == 'total_rewards_stop':
            usual_script.total_rewards_stop()
        elif check_result['name'] == 'total_rewards_stop_1':
            usual_script.total_rewards_stop_1()



        time_function.reduce_frequency(start_time, 1)
    return

stop_event = threading.Event()
is_pause = True
def start():
    check_result_max = category_index.check_main(['start_sorties'])
    if check_result_max['name'] == "unknown":
        global text_label
        text_label.config(text=f"Please\n{text_label.cget('text')}")
        return
    
    global stop_event, is_pause
    stop_event.clear()
    threading.Thread(target=run_loop, args=(stop_event, )).start()
    start_button.config(text="Pause")
    text_label.config(text="running...")
    is_pause = False

    return

def stop():
    global is_pause
    print("stopping")
    stop_event.set()
    start_button.config(text="Start")
    text_label.config(text="change to start screen\nand press start")
    is_pause = True
    return