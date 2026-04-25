
from tkinter import *

# Create the main window
root = Tk()

# Scrollbar setup
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=1000, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure the scrollbar to control the second canvas
scrollbar.config(command=secondCanvas.yview)

# Add widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# More widgets for testing scrolling capability
for i in range(30):
    Label(firstCanvas, text=f"Label {i+1}").pack()

# Add widgets to the second canvas
for i in range(50):
    Label(secondCanvas, text=f"Entry {i+1}").pack()

# Running the application
mainloop()
