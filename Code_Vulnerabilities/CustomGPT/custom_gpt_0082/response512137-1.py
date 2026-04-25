
from tkinter import *

root = Tk()

# Create Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create Frame to hold both canvases
frame = Frame(root)
frame.pack(side="left")

# Create the first canvas
firstCanvas = Canvas(frame, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(frame, width=200, height=400, scrollregion=(0, 0, 200, 600)) # Adjust scrollregion
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a vertical scrollbar that controls both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Connect scrollbar to canvases
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Add widgets to the first canvas
for i in range(10):
    widget = Label(firstCanvas, text=f'Label {i}')
    widget.pack()

# Add widgets to the second canvas to test scrolling
for i in range(50):
    widget = Label(secondCanvas, text=f'Spam {i}')
    widget.pack()

mainloop()
