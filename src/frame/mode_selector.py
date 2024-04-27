import tkinter as tk

from frame import debug_mode
from function import frame as frame_function


frame = None
debug_mode_button = None

def init_frame(import_app):
    global frame
    if frame is None:
        frame = tk.Frame(import_app)

        # init widgets
        global debug_mode_button
        debug_mode_button = tk.Button(frame, text="debug mode", command=debug_mode_button_active)
        debug_mode_button.grid(row=0, column=0)

def debug_mode_button_active():
    frame_function.swap_frame(frame, debug_mode.frame)
    debug_mode.start()
    return


    

#     # ---
# # init select_frame
# select_frame = tk.Frame(app)
# # create button
# debug_mode_button = tk.Button(select_frame, text="debug mode", command=debug_mode_active)
# # ---