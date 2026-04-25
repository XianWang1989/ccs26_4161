
from tkinter import *

def update_scroll(*args):
    # Update both canvases' views based on the scrollbar's value
    firstCanvas.yview(*args)
    secondCanvas.yview(*args)

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Create content for the first canvas
for i in range(20):
    label = Label(firstCanvas, text=f"Label {i + 1}")
    firstCanvas.create_window(100, 20 + i * 30, window=label)

# Create content for the second canvas
for i in range(50):
    entry = Entry(secondCanvas)
    secondCanvas.create_window(100, 20 + i * 30, window=entry)

# Configure scrollbar
scrollbar.config(command=update_scroll)
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

mainloop()
