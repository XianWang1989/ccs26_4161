
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400, bg="lightgray")
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas with a larger scroll region
secondCanvas = Canvas(root, width=200, height=400, bg="lightblue", scrollregion=(0, 0, 200, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Link the scrollbar to both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Add widgets to the first canvas
for i in range(20):
    Label(firstCanvas, text=f"Label {i}").pack()

# Add a long widget in the second canvas
for i in range(100):
    Label(secondCanvas, text=f"Second Label {i}").pack()

mainloop()
