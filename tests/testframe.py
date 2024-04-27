import tkinter as tk

import debug_mode
import start_frame
import mode_selector

app = tk.Tk()

# debug_mode.init_frame(app)
# debug_mode.frame.pack()

# start_frame.init_frame(app)
# start_frame.frame.pack()

mode_selector.init_frame(app)
mode_selector.frame.pack()


app.geometry("300x150")
app.mainloop()