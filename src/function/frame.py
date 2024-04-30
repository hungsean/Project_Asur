import tkinter as tk

def swap_frame(
    closing_frame: tk.Frame,
    opening_frame: tk.Frame
):
    if opening_frame is None:
        raise ValueError("opening_frame is None @frame.swap_frame")
    closing_frame.pack_forget()
    opening_frame.pack()