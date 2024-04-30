import ctypes

# Load gdi32 and user32
gdi32 = ctypes.windll.gdi32
user32 = ctypes.windll.user32

def get_screen_resolution(screen_num):
    # Create a device context for the specified screen
    hdc = user32.GetDC(screen_num)

    # Get the size of the screen
    width = gdi32.GetDeviceCaps(hdc, 8)  # HORZRES
    height = gdi32.GetDeviceCaps(hdc, 10)  # VERTRES

    # Release the device context
    user32.ReleaseDC(screen_num, hdc)

    return width, height

# Assume screens are numbered 0, 1, 2, ..., N-1
num_screens = ctypes.windll.user32.GetSystemMetrics(80)  # Number of screens
screen_resolutions = [get_screen_resolution(i) for i in range(num_screens)]

print(screen_resolutions)
for index, res in enumerate(screen_resolutions):
    print(f"Screen {index} resolution: {res[0]}x{res[1]}")

# import ctypes

# def get_scaling_factor(screen_index):
#     # Load gdi32 and user32
#     gdi32 = ctypes.windll.gdi32
#     user32 = ctypes.windll.user32

#     # Create a device context for the primary screen
#     hdc = user32.GetDC(screen_index)

#     # Get the logical DPI (dots per inch)
#     logical_dpi = gdi32.GetDeviceCaps(hdc, 88)  # LOGPIXELSX for horizontal DPI

#     # Release the device context
#     user32.ReleaseDC(screen_index, hdc)

#     # The default DPI in Windows is usually 96 DPI. Scaling factor is the ratio of current DPI to default DPI.
#     scaling_factor = logical_dpi / 96
#     return scaling_factor

# # Example of using the function to get scaling factor
# screen_index = 1  # Typically 0 for the primary screen
# scaling_factor = get_scaling_factor(screen_index)
# print(f"Scaling Factor: {scaling_factor}x ({int(scaling_factor * 100)}%)")

# from screeninfo import get_monitors, Enumerator
# for m in get_monitors(Enumerator.OSX):
#     print(str(m))

# import tkinter as tk

# root = tk.Tk()

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# print(screen_width )
# print(screen_height)