
from tkinter import *

root = Tk()

# Create the scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=200)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas with scroll region
secondCanvas = Canvas(root, width=200, height=200, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create content for the first canvas
for i in range(20):
    widget = Label(firstCanvas, text=f'This is label {i + 1}')
    widget.pack()

# Create content for the second canvas
for i in range(50):
    widget = Label(secondCanvas, text=f'Spam {i + 1}')
    widget.pack()

# Configure the scrollbar to control the second canvas
scrollbar.config(command=secondCanvas.yview)

# Maintain the canvas view with proper scroll regions
firstCanvas.update_idletasks()
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
