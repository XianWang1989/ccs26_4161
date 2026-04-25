
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 1000))
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create content for the first canvas
for i in range(30):
    widget = Label(firstCanvas, text=f'This is label {i + 1}')
    widget.pack()

# Create content for the second canvas
for j in range(30):
    widget = Label(secondCanvas, text=f'This is label {j + 1}')
    widget.pack()

# Configure scrollbar to scroll both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

mainloop()
