
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Frames to contain canvases
frame = Frame(root)
frame.pack(side='left', fill='both', expand=True)

# First Canvas
firstCanvas = Canvas(frame, width=200, height=400)
firstCanvas.pack(side='left', fill='both', expand=True)

# Second Canvas
secondCanvas = Canvas(frame, width=200, height=400, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side='left', fill='both', expand=True)

# Connecting scrollbar to both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding some sample widgets to both canvases
for i in range(30):
    widget = Label(firstCanvas, text=f'Spam {i}')
    widget.pack()

for i in range(30):
    widget = Label(secondCanvas, text=f'Another Spam {i}')
    widget.pack()

# Make sure the second canvas is scrollable
secondCanvas.create_rectangle((0, 0, 200, 5000))

mainloop()
