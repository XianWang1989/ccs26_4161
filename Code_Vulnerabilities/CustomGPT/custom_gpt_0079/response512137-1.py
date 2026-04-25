
from tkinter import *

# Create the main window
root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas with a scroll region
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0,0,0,1000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a scrollbar command for the second canvas
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding widgets to the first canvas
for i in range(20):
    widget = Label(firstCanvas, text=f"Label {i+1}")
    widget.pack()

# Adding widgets to the second canvas
for i in range(50):
    widget = Label(secondCanvas, text=f"Entry {i+1}")
    widget.pack()

# Create a rectangle in the second canvas
secondCanvas.create_rectangle(50, 300, 150, 600, fill="blue")

# Start the Tkinter main loop
mainloop()
