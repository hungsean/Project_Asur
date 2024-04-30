import mss
import tkinter as tk
import time
import cv2
import numpy as np
import pyautogui

def capture_specific_area(top, left, width, height, interval=5, filename='screenshot.png'):
    """
    Capture a specific area of the screen at a set interval.

    :param top: The top pixel of the capture area.
    :param left: The left pixel of the capture area.
    :param width: The width of the capture area.
    :param height: The height of the capture area.
    :param interval: Time in seconds between captures.
    :param filename: The filename to save the screenshot.
    """
    with mss.mss() as sct:
        # Define the bbox of the area. bbox format: (left, top, width, height)
        # bbox = (left, top, left + width, top + height)

        while True:
            # Capture the screen
            sct_img = sct.shot(mon=3, output="screenshot.png")
            
            # # Convert to cv2 image
            # img = np.array(sct_img)
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # # Save the image
            # cv2.imwrite(filename, img)
            # print(f'Screenshot saved as {filename}')
            
            # Wait for the specified interval
            time.sleep(interval)

# Example usage: capture a 800x600 area starting from the top-left corner (0, 0)
# capture_specific_area(0, 0, 800, 600, interval=1, filename='screenshot.png')

# def screenshot(screen_index):
#     with mss.mss() as sct:
#         sct.shot(mon=(screen_index+1), output="assets\\screenshots\\temp.png")
#         screenshot_np = cv2.imread("assets\\screenshots\\temp.png")
#         return screenshot_np
    
def screenshot(screen_index: int):
    with mss.mss() as sct:
        print(sct.monitors)
        monitor = sct.monitors[screen_index+1]
        sct_img = sct.grab(monitor)
        img_np = np.array(sct_img)
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)  # 從BGRA轉為BGR
        return img_np

# import image_process
# image = image_process.screenshot(0)
image = screenshot(0)
cv2.imshow('image', image)
cv2.waitKey(0)