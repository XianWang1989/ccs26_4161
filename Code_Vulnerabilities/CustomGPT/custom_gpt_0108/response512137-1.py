
from tkinter import *

root = Tk()

# Create the scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Create some widgets in the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Add multiple widgets to firstCanvas
for i in range(20):
    Label(firstCanvas, text=f"Widget {i + 1}").pack()

# Create a rectangle in the second canvas
secondCanvas.create_rectangle(50, 50, 150, 2500)

# Add widgets to the second canvas
for i in range(20):
    Entry(secondCanvas).pack()

# Configure the scrollbar to control both canvases
def on_scroll(*args):
    firstCanvas.yview(*args)
    secondCanvas.yview(*args)

scrollbar.config(command=on_scroll)
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Start the main loop
mainloop()
