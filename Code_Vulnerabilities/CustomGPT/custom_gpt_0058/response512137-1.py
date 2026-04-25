
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=10000, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a rectangle in the second canvas
secondCanvas.create_rectangle((200, 300, 300, 6000))

# Add widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Lots of widgets on the first canvas
widgetOne = Label(firstCanvas, text="this is a test")
widgetOne.pack()
widgetTwo = Entry(firstCanvas)
widgetTwo.pack()
widgetThree = Label(secondCanvas, text='Spam')
widgetThree.pack()
widgetFour = Entry(secondCanvas)
widgetFour.pack()   

# Configure scrollbar to control the second canvas and set its command
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

mainloop()
