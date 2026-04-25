
from tkinter import *

root = Tk()

# Create a frame to hold both canvases and the scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

# Create and configure the scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(frame, width=200, height=400)
firstCanvas.pack(side="left", fill=BOTH, expand=True)

# Create the second canvas
secondCanvas = Canvas(frame, width=200, height=400)
secondCanvas.pack(side="left", fill=BOTH, expand=True)

# Linking the scrollbar to the second canvas
secondCanvas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=secondCanvas.yview)

# Create a scroll region for the second canvas
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

# Add content to the first canvas
for i in range(20):  # Just adding multiple labels as an example
    widget = Label(firstCanvas, text=f'Test Label {i+1}')
    widget.pack()

# Add content to the second canvas
for i in range(50):  # More content to demonstrate scrolling
    widget = Label(secondCanvas, text=f'More Test Label {i+1}')
    widget.pack()

# Create a rectangle on the second canvas
secondCanvas.create_rectangle(0, 0, 200, 200, outline="black") # Just an example rectangle

# Need to set scrollregion to encompass all elements in the second canvas
secondCanvas.update_idletasks()  # Update "to calculate" the canvas size
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

# Start the application
mainloop()
