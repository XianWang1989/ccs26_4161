
from tkinter import *

def on_configure(event):
    # Update the scroll region of the canvas to encompass the inner elements
    secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

root = Tk()

# Scroll Bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Bind the configuration event to update scrollregion
secondCanvas.bind("<Configure>", on_configure)

# Example widgets in the first canvas
for i in range(30):
    widget = Label(firstCanvas, text=f'Label {i}')
    widget.pack()

# Example widgets in the second canvas
for i in range(50):
    widget = Label(secondCanvas, text=f'Section {i}')
    widget.pack()

# Scrollbar command
scrollbar.config(command=secondCanvas.yview)

mainloop()
