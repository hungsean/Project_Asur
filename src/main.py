import tkinter as tk

from frame import start as start_frame
from frame import mode_selector as mode_selector_frame
from frame import debug_mode as debug_mode_frame
from frame import auto_stage as auto_stage_frame




app = tk.Tk()
app.title("Screen Selector")

start_frame.init_frame(app)
mode_selector_frame.init_frame(app)
debug_mode_frame.init_frame(app)
auto_stage_frame.init_frame(app)
start_frame.frame.pack()


if start_frame.isSingleScreen():
    print("[ERROR] only one monitor!")
    exit()

app.geometry("300x150")
app.mainloop()
