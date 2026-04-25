
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=200, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=200, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Adding widgets to the first canvas
for i in range(20):  # Adding multiple labels to create enough content
    label = Label(firstCanvas, text=f'Spam {i+1}')
    label.pack()

# Adding widgets to the second canvas
for i in range(20):  # Adding multiple entry fields to create enough content
    entry = Entry(secondCanvas)
    entry.pack()

# Configure scrollbar to control both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

mainloop()
