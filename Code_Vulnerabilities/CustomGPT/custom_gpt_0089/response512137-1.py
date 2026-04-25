
from tkinter import *

# Create the main window
root = Tk()

# Create a vertical scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create two canvases
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

secondCanvas = Canvas(root, width=500, height=300, scrollregion=(0, 0, 0, 2000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Add content to the first canvas
for i in range(20):
    widget = Label(firstCanvas, text=f'This is item {i+1}')
    widget.pack()

# Add content to the second canvas
for i in range(50):
    widget = Label(secondCanvas, text=f'Spam {i+1}')
    widget.pack()

# Configure the scrollbar to scroll both canvases
def scroll_both(*args):
    firstCanvas.yview(*args)
    secondCanvas.yview(*args)

scrollbar.config(command=scroll_both)

# Start the application
mainloop()
