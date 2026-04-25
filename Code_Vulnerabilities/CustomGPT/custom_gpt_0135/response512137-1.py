
from tkinter import *

def setup_canvas(canvas, scrollbar):
    # Configure the scrollbar to control the canvas
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400)
secondCanvas.pack(side="left", fill="both", expand=True)

# Attach scrollbar to the second canvas
setup_canvas(secondCanvas, scrollbar)

# Creating content for the first canvas
for i in range(10):
    widget = Label(firstCanvas, text=f'This is label {i+1}')
    firstCanvas.create_window(100, i * 30, window=widget)

# Creating content for the second canvas
for i in range(50):
    widget = Label(secondCanvas, text=f'This is label from second canvas {i+1}')
    secondCanvas.create_window(100, i * 30, window=widget)

# Set the scroll region
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

mainloop()
