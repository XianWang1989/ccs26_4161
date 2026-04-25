
from tkinter import *

root = Tk()

# Create a frame to hold the canvases and scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

# Create a vertical scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas and link scrollbar
firstCanvas = Canvas(frame, width=300, height=400, yscrollcommand=scrollbar.set)
firstCanvas.pack(side="left", fill=BOTH, expand=True)

# Create the second canvas and link scrollbar
secondCanvas = Canvas(frame, width=300, height=400, scrollregion=(0, 0, 0, 3000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill=BOTH, expand=True)

# Connect scrollbar to both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Adding labels and entries to the first canvas
for i in range(20):
    Label(firstCanvas, text=f'This is label {i}').pack()

# Adding labels and entries to the second canvas
for i in range(20):
    Label(secondCanvas, text=f'This is label {i + 20}').pack()

mainloop()
