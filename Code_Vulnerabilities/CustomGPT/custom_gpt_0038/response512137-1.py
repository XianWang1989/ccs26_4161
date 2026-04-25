
from tkinter import *

root = Tk()

# Create scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=300, scrollregion=(0,0,0,5000))
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0,0,0,5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbar to both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Add widgets to first canvas
for i in range(20):
    Label(firstCanvas, text=f"Label {i}").pack()

# Add widgets to second canvas
for i in range(20):
    Entry(secondCanvas).pack()

mainloop()
