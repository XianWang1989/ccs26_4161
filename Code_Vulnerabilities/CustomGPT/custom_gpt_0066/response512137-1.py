
from tkinter import *

root = Tk()

# Create a frame to hold both canvases and the scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

# Scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(frame, width=200, height=400)
firstCanvas.pack(side="left", fill=BOTH, expand=True)

# Second Canvas
secondCanvas = Canvas(frame, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill=BOTH, expand=True)

# Create a vertical scrollbar linked to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Add content to the first canvas
for i in range(20):
    label = Label(firstCanvas, text=f"Label {i+1}")
    label.pack()

# Add content to the second canvas
for i in range(100):
    label = Label(secondCanvas, text=f"Spam {i+1}")
    label.pack()

# Create a rectangle in the second canvas for demonstration
secondCanvas.create_rectangle(50, 0, 150, 600)

root.mainloop()
