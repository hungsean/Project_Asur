# import tkinter as tk

# # import debug_mode
# # import start_frame
# # import mode_selector

# app = tk.Tk()


# def draw_rectangle(x1, y1, x2, y2, duration, color='red'):
#     # 創建一個新視窗
#     new_window = tk.Toplevel()
#     new_window.attributes('-fullscreen', True)  # 設置全螢幕模式

#     # 創建一個 Canvas 小工具，覆蓋整個螢幕
#     canvas = tk.Canvas(new_window, width=new_window.winfo_screenwidth(), height=new_window.winfo_screenheight())
#     canvas.pack()

#     # 繪製長方形
#     rect = canvas.create_rectangle(x1, y1, x2, y2, outline=color, fill="")

#     # 設定定時器，自動關閉窗口
#     new_window.after(duration, new_window.destroy)

# draw_rectangle(-1620, 500, -1400, 600, 10)
# app.geometry("300x150")
# app.mainloop()

import tkinter as tk
from screeninfo import get_monitors
import time

def create_transparent_window(screen_index, point1, point2):
    
    # 獲取螢幕資訊
    monitors = get_monitors()
    if screen_index < 0 or screen_index >= len(monitors):
        print("Invalid screen index.")
        return

    # 取得指定螢幕的大小和位置
    screen = monitors[screen_index]
    screen_width = screen.width
    screen_height = screen.height
    screen_x = screen.x
    screen_y = screen.y

    start_point_x = screen_x + point1[0]
    start_point_y = screen_y + point1[1]
    end_point_x = screen_x + point2[0]
    end_point_y = screen_y + point2[1]


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

# 測試函數
if __name__ == "__main__":
    screen_index = 1  # 指定的螢幕索引
    point1 = (100, 100)  # 第一個座標點 (x1, y1)
    point2 = (300, 300)  # 第二個座標點 (x2, y2)
    create_transparent_window(screen_index, point1, point2)
