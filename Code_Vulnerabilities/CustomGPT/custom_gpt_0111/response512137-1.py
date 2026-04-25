
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 1000))
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 1000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Creating some content for both canvases
for i in range(30):
    Label(firstCanvas, text=f"Label {i}").pack()
    Label(secondCanvas, text=f"Label {i}").pack()

# Configure scrollbar to control both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Setting yscrollcommand for both canvases
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

mainloop()
