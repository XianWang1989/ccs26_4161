
from tkinter import *

def on_canvas_configure(event):
    # Update the scrollregion of the second canvas when its content changes
    secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create content on the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Adding lots of widgets to the first canvas
for i in range(20):
    Label(firstCanvas, text=f"Label {i}").pack()

# Create content on the second canvas
for i in range(50):
    Label(secondCanvas, text=f"This is a test {i}").pack()

# Configure scrollbar command
scrollbar.config(command=secondCanvas.yview)

# Update the scrollregion to encompass all widgets
secondCanvas.bind("<Configure>", on_canvas_configure)

mainloop()
