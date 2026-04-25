
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 2000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Connecting scrollbar to the canvas
scrollbar.config(command=secondCanvas.yview)

# Adding content to the first canvas
for i in range(10):
    widget = Label(firstCanvas, text=f'Spam {i+1}')
    widget.pack()

# Adding content to the second canvas
for i in range(50):
    widget = Label(secondCanvas, text=f'This is test {i+1}')
    widget.pack()

# Adding a rectangle for visual reference in the second canvas
secondCanvas.create_rectangle((20, 20, 180, 800), outline="black", fill="lightgrey")

mainloop()
