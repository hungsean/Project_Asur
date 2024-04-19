import tkinter as tk
global select_start_x 
global select_start_y
global select_end_x 
global select_end_y

class FullScreenRectSelector:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)  # Fullscreen mode
        self.root.attributes('-alpha', 0.3)  # Set transparency
        self.root.configure(bg='black')  # Black background which will be seen as transparent
        
        self.canvas = tk.Canvas(self.root, cursor="cross", bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.rect = None
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red') # 框線

    def on_drag(self, event):
        curX, curY = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_release(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y= self.canvas.canvasy(event.y)
        print(f"Start: ({self.start_x}, {self.start_y})")
        print(f"End: ({self.end_x}, {self.end_y})")
        

        select_start_x = self.start_x
        select_start_y = self.start_y
        select_end_x = self.end_x
        select_end_y = self.end_y

        self.root.destroy()  # Close the overlay after selection

    def run(self):
        self.root.mainloop()

def start_select():
    global app
    app = FullScreenRectSelector()
    app.run()
    return (app.start_x, app.start_y), (app.end_x, app.end_y)

    # 返回起點和終點座標
    # return (app.start_x, app.start_y), (app.end_x, app.end_y)
        
