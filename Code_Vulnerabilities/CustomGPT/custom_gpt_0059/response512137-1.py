
from tkinter import *

def create_gui():
    root = Tk()

    # Scrollbar
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    # First Canvas
    first_canvas = Canvas(root, width=200, height=400)
    first_canvas.pack(side="left", fill="both", expand=True)

    # Second Canvas
    second_canvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000))
    second_canvas.pack(side="left", fill="both", expand=True)

    # Configure scrollbar to control both canvases
    def on_scroll(*args):
        first_canvas.yview(*args)
        second_canvas.yview(*args)

    scrollbar.config(command=on_scroll)

    # Create some widgets in the first canvas
    for i in range(30):
        Label(first_canvas, text=f"Label {i+1}").pack()

    # Create some widgets in the second canvas
    for i in range(100):
        Label(second_canvas, text=f"Second Canvas Label {i+1}").pack()

    # Set the scroll commands for the canvases
    first_canvas.config(yscrollcommand=scrollbar.set)
    second_canvas.config(yscrollcommand=scrollbar.set)

    root.mainloop()

create_gui()
