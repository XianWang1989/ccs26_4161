
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure scrollbar
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Sample widgets for the first canvas
for i in range(20):
    widget = Label(firstCanvas, text=f'Spam {i}')
    widget.pack()

# Sample widgets for the second canvas
for i in range(50):
    widget = Label(secondCanvas, text=f'Spam Entry {i}')
    widget.pack()

mainloop()
