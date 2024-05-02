import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors

from frame import mode_selector
from function import frame as frame_function

monitors = get_monitors()
screen_names = [f"Screen {i+1}: {m.width}x{m.height}" for i, m in enumerate(monitors)]
# screen_names = [f"Screen {i}" for i in range(len(monitors))]
monitor_index = 0

frame = None
selector = None
start_button = None

def init_frame(import_app):
    global frame
    if frame is None:
        frame = tk.Frame(import_app)

        # init widgets
        global selector, screen_names
        selector = ttk.Combobox(frame, values=screen_names, state="readonly")
        selector.pack(pady=20, padx=20)
        selector.bind("<<ComboboxSelected>>", update_screen_info)
        global start_button
        start_button = tk.Button(frame, text="start", command=start_button_active, state="disabled")
        start_button.pack(padx=20,pady=20)

def start_button_active():
    # if mode_selector.frame is None:
    #     print("[ERROR] mode_selector frame is None @start.start_button_active")
    #     return
    # frame.pack_forget()
    # mode_selector.frame.pack()
    frame_function.swap_frame(frame, mode_selector.frame)
    return

def update_screen_info(event):
    global monitor_index
    monitor_index = selector.current()
    print("[INFO] monitor index: ", monitor_index)
    start_button.config(state="normal")

def isSingleScreen():
    if len(monitors) == 1:
        return True
    else:
        return False

# ---
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
# ---

    