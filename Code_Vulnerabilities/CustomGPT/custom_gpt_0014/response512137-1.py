
from tkinter import *

root = Tk()

# Configure the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 200, 300))
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbar to both canvases
def on_scroll(*args):
    firstCanvas.yview(*args)
    secondCanvas.yview(*args)

scrollbar.config(command=on_scroll)

# Add content to the first canvas
for i in range(20):
    widget = Label(firstCanvas, text=f'Label {i+1}')
    widget.pack()

# Add content to the second canvas
for i in range(20):
    widget = Label(secondCanvas, text=f'Label {i+1}')
    widget.pack()

# Optional: Set the scrollbar to scroll both canvases
firstCanvas.configure(yscrollcommand=scrollbar.set)
secondCanvas.configure(yscrollcommand=scrollbar.set)

mainloop()
