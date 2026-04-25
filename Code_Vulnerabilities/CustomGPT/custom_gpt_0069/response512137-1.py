
from tkinter import *

root = Tk()
root.geometry("400x400")

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas with scroll region
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 200, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Scrollbar configuration
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding widgets to the first canvas
for i in range(20):
    label = Label(firstCanvas, text=f'This is item {i}')
    label.pack()

# Adding widgets to the second canvas
for i in range(50):
    entry = Entry(secondCanvas)
    entry.insert(0, f'Text entry {i}')
    entry.pack()

# Make sure to configure the scroll region of the second canvas
secondCanvas.update_idletasks()  # Update the canvas to calculate the scroll region

mainloop()
