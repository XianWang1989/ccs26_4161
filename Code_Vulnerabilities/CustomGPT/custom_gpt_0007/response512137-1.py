
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Adding content to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Lots of widgets so they reach beyond the screen
widgetOne = Label(firstCanvas, text="This is a test")
widgetOne.pack()
widgetTwo = Entry(firstCanvas)
widgetTwo.pack()
widgetThree = Label(secondCanvas, text='Spam')
widgetThree.pack()
widgetFour = Entry(secondCanvas)
widgetFour.pack()   

# Configure scrollbar to control the second canvas
scrollbar.config(command=secondCanvas.yview)

# Update the first canvas to react to scrollbar by linking both canvases
def scroll(*args):
    firstCanvas.yview(*args)
    secondCanvas.yview(*args)

scrollbar.config(command=scroll)

mainloop()
