
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=100, bg='lightblue')
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas with the scrollregion set appropriately
secondCanvas = Canvas(root, width=200, height=100, bg='lightgreen')
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a vertical scroll region for secondCanvas
secondCanvas.config(scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)

# Linking the scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Create some widgets
widget = Label(firstCanvas, text='This is a test of the scrollbar', bg='lightblue')
widget.pack()

# Add several widgets to firstCanvas
for i in range(20):  # Create multiple test labels
    Label(firstCanvas, text=f"Label {i}", bg='lightblue').pack()

# Create widget content for secondCanvas
for i in range(100):  # Create multiple test entries
    Entry(secondCanvas).pack()

# Draw a rectangle in secondCanvas (this is optional)
secondCanvas.create_rectangle((200, 300, 300, 6000), outline='black')

# Make sure each canvas is linked to the scrollbar
firstCanvas.config(yscrollcommand=lambda *args: scrollbar.set(*args))
secondCanvas.config(yscrollcommand=scrollbar.set)

# Set scrollbar command to update both canvases
def scroll(*args):
    firstCanvas.yview(*args)  # Scroll first canvas
    secondCanvas.yview(*args)  # Scroll second canvas

scrollbar.config(command=scroll)

mainloop()
