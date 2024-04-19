import tkinter as tk
from garbage.screen_position import *

def on_button_click():
    print("Button clicked, closing window and returning 1")
    window.destroy()
    global return_value
    show_select()
    return_value = 1

def show_button():
    global window
    window = tk.Tk()
    window.title("Show Button Window")
    tk.Button(window, text="Click Me", command=on_button_click).pack()
    window.mainloop()
    return return_value

def show_select():
    ((select_start_x, select_start_y), (select_end_x, select_end_y)) = start_select()
    print("select_start_x: ", select_start_x)
    print("select_start_y: ", select_start_y)
    print("select_end_x: ", select_end_x)
    print("select_end_y: ", select_end_y)

# 主程式
return_value = 0  # 初始化返回值
show_button()  # 顯示按鈕並等待按鈕被點擊
# show_select()
print(f"Returned value: {return_value}")  # 打印返回值，確認按鈕點擊後的操作
