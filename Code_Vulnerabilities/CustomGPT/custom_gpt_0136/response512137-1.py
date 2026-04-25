
from tkinter import *

root = Tk()
root.geometry("400x400")

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 200, 1000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link the scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Create content in the first canvas
for i in range(10):
    widget = Label(firstCanvas, text=f'Label {i+1}')
    widget.pack()

# Create lots of widgets in the second canvas
for i in range(30):
    widget = Label(secondCanvas, text=f'Label {i+1}')
    widget.pack()

# Update the scrollregion of the second canvas to ensure all content is scrollable
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

mainloop()
