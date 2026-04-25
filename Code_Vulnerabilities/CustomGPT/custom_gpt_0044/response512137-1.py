
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas - setting scrollregion properly
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create Rectangle for visualization
secondCanvas.create_rectangle(0, 0, 200, 5000, fill='lightgrey')

# Add widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Adding more widgets
for i in range(20):  # Add multiple labels to demonstrate scrolling
    widget = Label(firstCanvas, text=f"Label {i+1}")
    widget.pack()

# Add widgets to the second canvas
for i in range(50):  # More widgets on the second canvas
    widget = Label(secondCanvas, text=f"Entry {i+1}")
    widget.pack()

# Configure the scrollbar
scrollbar.config(command=secondCanvas.yview)

mainloop()
