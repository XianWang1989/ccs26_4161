
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Connect scrollbars with canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Widgets on the first canvas
for i in range(20):  # Add some labels to demonstrate scrolling
    label = Label(firstCanvas, text=f'This is label {i + 1}')
    firstCanvas.create_window(100, 25 * i, window=label)

# Widgets on the second canvas
for i in range(50):  # Add some labels to demonstrate scrolling
    label = Label(secondCanvas, text=f'This is label {i + 1}')
    secondCanvas.create_window(100, 25 * i, window=label)

mainloop()
