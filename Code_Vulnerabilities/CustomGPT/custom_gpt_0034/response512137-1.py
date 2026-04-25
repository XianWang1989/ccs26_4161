
from tkinter import *

root = Tk()

# Scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a rectangle in the second canvas
secondCanvas.create_rectangle((0, 0, 200, 5000), fill='lightblue')

# Adding widgets to the first canvas
widgets = [
    Label(firstCanvas, text='This is a test label 1'),
    Entry(firstCanvas),
    Label(firstCanvas, text='This is a test label 2'),
    Entry(firstCanvas),
    Label(firstCanvas, text='This is a test label 3'),
    Entry(firstCanvas)
]

for widget in widgets:
    widget.pack(in_=firstCanvas)

# Configuring the scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

mainloop()
