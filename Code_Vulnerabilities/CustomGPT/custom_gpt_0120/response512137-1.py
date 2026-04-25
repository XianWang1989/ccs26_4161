
from tkinter import *

def on_scroll(*args):
    firstCanvas.yview(*args)
    secondCanvas.yview(*args)

root = Tk()

# Creating the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 5000))
firstCanvas.pack(side="left", fill="both", expand=True)
firstCanvas.config(yscrollcommand=scrollbar.set)

# Second canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Link scrollbar to both canvases
scrollbar.config(command=on_scroll)

# Adding widgets to the first canvas
for i in range(20):
    Label(firstCanvas, text=f"This is label {i + 1}").pack()

# Adding widgets to the second canvas
for i in range(50):
    Entry(secondCanvas, width=25).pack()

mainloop()
