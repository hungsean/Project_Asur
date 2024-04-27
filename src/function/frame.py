

def swap_frame(closing_frame, opening_frame):
    if opening_frame is None:
        raise ValueError("opening_frame is None @frame.swap_frame")
    closing_frame.pack_forget()
    opening_frame.pack()
    return