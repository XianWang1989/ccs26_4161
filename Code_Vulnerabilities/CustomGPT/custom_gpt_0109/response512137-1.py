
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=500)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 1500))
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding widgets to the first canvas
for i in range(20):
    widget = Label(firstCanvas, text=f'Item {i+1}')
    widget.pack()

# Adding widgets to the second canvas
for j in range(30):
    widget = Label(secondCanvas, text=f'Scrollable Item {j+1}')
    widget.pack()

# Create a rectangle in the second canvas
secondCanvas.create_rectangle((0, 0, 200, 1500), outline="black")

mainloop()
