
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=600)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=600, scrollregion=(0, 0, 200, 2000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Connect scrollbar to both canvases
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Adding widgets to firstCanvas
for i in range(30):
    Label(firstCanvas, text=f'Label {i}').pack()

# Adding widgets to secondCanvas
for i in range(30):
    Label(secondCanvas, text=f'Second Canvas Label {i}').pack()

mainloop()
