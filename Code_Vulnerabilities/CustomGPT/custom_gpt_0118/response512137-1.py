
from tkinter import *

def on_canvas_configure(event):
    # Update the scrollregion of the canvas
    firstCanvas.configure(scrollregion=firstCanvas.bbox("all"))
    secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Bind the configuration of the canvas to the scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Add content to firstCanvas
for i in range(20):
    widget = Label(firstCanvas, text=f'This is a test label {i}')
    widget.pack()

# Add content to secondCanvas
for i in range(50):
    entry = Entry(secondCanvas)
    entry.pack()

# Update the scrollregions
firstCanvas.bind("<Configure>", on_canvas_configure)
secondCanvas.bind("<Configure>", on_canvas_configure)

mainloop()
