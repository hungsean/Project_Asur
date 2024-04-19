import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors

def update_screen_info(event):
    monitor_index = screen_selector.current()
    selected_monitor = monitors[monitor_index]
    info_label.config(text=f"Screen {monitor_index+1}: {selected_monitor.width} x {selected_monitor.height}")

app = tk.Tk()
app.title("Screen Selector")

# 獲取所有螢幕的資訊
monitors = get_monitors()
print(monitors)
screen_names = [f"Screen {i+1}: {m.width}x{m.height}" for i, m in enumerate(monitors)]

# 下拉選單讓用戶選擇螢幕
screen_selector = ttk.Combobox(app, values=screen_names, state="readonly")
screen_selector.pack(pady=20)
screen_selector.bind("<<ComboboxSelected>>", update_screen_info)

# 顯示選定螢幕的資訊
info_label = tk.Label(app, text="Select a screen to see its resolution")
info_label.pack(pady=10)

app.mainloop()
