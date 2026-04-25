
from tkinter import *

# Create the main window
root = Tk()

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure the scrollbar
scrollbar.config(command=secondCanvas.yview)

# Link scrollbar with the vertical view of the second canvas
secondCanvas.config(yscrollcommand=scrollbar.set)

# Add content to the first canvas
widget = Label(firstCanvas, text='Label 1')
widget.pack()

# Adding multiple widgets to firstCanvas
for i in range(10):
    Label(firstCanvas, text=f"This is label {i + 1}").pack()

# Add content to the second canvas
for i in range(20):
    Label(secondCanvas, text=f"This is a label from the second canvas {i + 1}").pack()

# Create a large rectangle in the second canvas for visibility
secondCanvas.create_rectangle((20, 20, 180, 1000), outline="blue")

# Start the main loop
mainloop()
