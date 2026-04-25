
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000))
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbar to both canvases
def on_scroll(*args):
    firstCanvas.yview(*args)
    secondCanvas.yview(*args)

scrollbar.config(command=on_scroll)
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding widgets to first canvas
for i in range(30):
    label = Label(firstCanvas, text=f"Label {i+1}")
    firstCanvas.create_window(100, 20 + i * 30, window=label)

# Adding widgets to second canvas
for i in range(50):
    label = Label(secondCanvas, text=f"Entry {i+1}")
    secondCanvas.create_window(100, 20 + i * 30, window=label)

mainloop()
