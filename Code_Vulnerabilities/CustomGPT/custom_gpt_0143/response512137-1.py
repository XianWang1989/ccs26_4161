
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=5000, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Connect the scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Add widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Add more widgets
widgetOne = Label(firstCanvas, text="this is a test")
widgetOne.pack()

widgetTwo = Entry(firstCanvas)
widgetTwo.pack()

# Add widgets to the second canvas
widgetThree = Label(secondCanvas, text='Spam')
widgetThree.pack()

widgetFour = Entry(secondCanvas)
widgetFour.pack()

# Start the main loop
mainloop()
