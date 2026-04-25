
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 800))
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 800))
secondCanvas.pack(side="left", fill="both", expand=True)

# Linking scrollbar to both canvases
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Create widgets for first canvas
for i in range(20):
    Label(firstCanvas, text=f'Label {i}').pack()

# Create widgets for second canvas
for i in range(20):
    Label(secondCanvas, text=f'Second Label {i}').pack()

# Set the scrollbars' yscrollcommand to update both canvases
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

mainloop()
