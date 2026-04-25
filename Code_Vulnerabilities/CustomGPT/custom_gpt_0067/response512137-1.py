
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=500)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas with a large scroll region
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a rectangle in the second canvas
secondCanvas.create_rectangle((0, 0, 200, 5000), fill="lightblue")

# Add widgets to the first canvas
for i in range(20):  # Add multiple widgets to exceed the canvas height
    widget = Label(firstCanvas, text=f"Label {i + 1}")
    widget.pack()

# Link scrollbar to both canvases
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

mainloop()
