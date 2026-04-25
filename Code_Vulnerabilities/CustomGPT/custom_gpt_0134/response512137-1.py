
from tkinter import *

root = Tk()

# Create and pack the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 2000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create some content in the first canvas
for i in range(30):
    widget = Label(firstCanvas, text=f'This is label {i + 1}')
    widget.pack()

# Create some content in the second canvas
for i in range(50):
    widget = Label(secondCanvas, text=f'This is label {i + 1} in second canvas')
    widget.pack()

# Configure scrollbar to control the second canvas
scrollbar.config(command=secondCanvas.yview)

# Update the scroll region based on content
secondCanvas.update_idletasks()  # Update to get correct bounding box
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
