
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 1000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a rectangle in the second canvas
secondCanvas.create_rectangle(50, 300, 150, 600)

# Add widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Lots of widgets so they reach beyond the screen
for i in range(30):
    widgetOne = Label(firstCanvas, text=f"Label {i+1}")
    widgetOne.pack()

# Add widgets to the second canvas
for i in range(30):
    widgetTwo = Label(secondCanvas, text=f"Label {i+1 + 30}")
    widgetTwo.pack()

# Configure the scrollbar
scrollbar.config(command=lambda *args: (secondCanvas.yview(*args), firstCanvas.yview(*args)))

# Make sure to set valid scroll regions for both canvas if needed
firstCanvas.configure(scrollregion=firstCanvas.bbox("all"))
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

mainloop()
