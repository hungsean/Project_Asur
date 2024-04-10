import mss
import time
from PIL import Image
import cv2
import numpy as np

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
        bbox = (left, top, left + width, top + height)

        while True:
            # Capture the screen
            sct_img = sct.grab(bbox)
            
            # Convert to cv2 image
            img = np.array(sct_img)
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            
            # Save the image
            cv2.imwrite(filename, img)
            print(f'Screenshot saved as {filename}')
            
            # Wait for the specified interval
            time.sleep(interval)

# Example usage: capture a 800x600 area starting from the top-left corner (0, 0)
capture_specific_area(0, 0, 800, 600, interval=10, filename='screenshot.png')
