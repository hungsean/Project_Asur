import tkinter as tk

from frame import debug_mode, auto_stage
from function import frame as frame_function


frame = None
debug_mode_button = None
auto_stage_button = None
script_test_button = None

def init_frame(import_app):
    global frame
    if frame is None:
        frame = tk.Frame(import_app)

        # init widgets
        global debug_mode_button
        debug_mode_button = tk.Button(frame, text="debug mode", command=debug_mode_button_active)
        debug_mode_button.grid(row=0, column=0)

        global auto_stage_button
        auto_stage_button = tk.Button(frame, text="auto stage", command=auto_stage_button_active)
        auto_stage_button.grid(row=0, column=1)

        global script_test_button
        script_test_button = tk.Button(frame, text="test", command=script_text_button_active)
        script_test_button.grid(row=1, column=0)



def debug_mode_button_active():
    frame_function.swap_frame(frame, debug_mode.frame)
    debug_mode.start()
    return

def auto_stage_button_active():
    frame_function.swap_frame(frame, auto_stage.frame)
    return

from script import retired
def script_text_button_active():
    # TODO
    retired.main()
    return


