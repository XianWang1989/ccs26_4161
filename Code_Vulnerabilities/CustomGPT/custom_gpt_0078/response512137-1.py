
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=300, height=500)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=300, height=500, scrollregion=(0,0,0,5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Scrollbar configuration
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding content to first canvas
for i in range(10):
    label = Label(firstCanvas, text=f"Label {i+1}")
    label.pack()

# Adding content to second canvas
for i in range(10):
    widget = Label(secondCanvas, text=f"Widget {i+1}")
    widget.pack()

# Create a scrollable area for the second canvas
secondCanvas.create_window((0, 0), window=secondCanvas, anchor='nw')

root.mainloop()
