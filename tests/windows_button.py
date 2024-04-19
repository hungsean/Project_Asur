import tkinter as tk
from garbage.screen_position import *

async def on_button_click():
    # This is where the function to execute on button click will go.
    print("Button clicked!")
    root.withdraw()
    start_coords, end_coords = await start_select()
    print(f"Selected Area: Start {start_coords}, End {end_coords}")
    root.deiconify()
    return
    

# def on_window_resize(event):
#     # This function is called whenever the window is resized.
#     # It prints the current size of the window.
#     print(f"Window size: {event.width}x{event.height}")

# Create the main window
root = tk.Tk()
root.title("Button Example")
root.geometry("300x100")
# root.bind('<Configure>', on_window_resize)

# Create a button
button = tk.Button(root, text="Click Me", await on_button_click)

# Place the button in the window
button.pack()

# Start the GUI event loop
root.mainloop()
