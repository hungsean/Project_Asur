import tkinter as tk
import frame.start as start_frame
import time

def swap_frame(
    closing_frame: tk.Frame,
    opening_frame: tk.Frame
):
    if opening_frame is None:
        raise ValueError("opening_frame is None @frame.swap_frame")
    closing_frame.pack_forget()
    opening_frame.pack()

def create_transparent_window(point1, point2):
    

    # 取得指定螢幕的大小和位置
    screen = start_frame.monitors[start_frame.monitor_index]
    screen_width = screen.width
    screen_height = screen.height
    screen_x = screen.x
    screen_y = screen.y

    start_point_x = point1[0] - screen_x
    start_point_y = point1[1] - screen_y
    end_point_x = point2[0] - screen_x
    end_point_y = point2[1] - screen_y


    # 創建視窗
    window = tk.Tk()
    window.overrideredirect(True)  # 移除視窗邊框
    window.geometry(f"{screen_width}x{screen_height}+{screen_x}+{screen_y}")  # 設定視窗位置和大小
    window.attributes('-alpha', 0.3)  # 設定視窗透明度

    # 繪製矩形
    canvas = tk.Canvas(window, width=screen_width, height=screen_height, highlightthickness=0)
    canvas.pack()
    
    canvas.create_rectangle(start_point_x, start_point_y, end_point_x, end_point_y, outline="red", width=2)

    window.update()  # 更新視窗，使繪製的矩形可見

    # 等待一段時間
    time.sleep(3)  # 這裡的5代表等待5秒，可以根據需求更改

    # 刪除視窗
    window.destroy()