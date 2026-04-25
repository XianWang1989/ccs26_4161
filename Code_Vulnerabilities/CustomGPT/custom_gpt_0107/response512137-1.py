
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Link canvases to scrollbar
secondCanvas.config(yscrollcommand=scrollbar.set)

# Create rectangles and widgets in the first canvas
widgetOne = Label(firstCanvas, text="This is a test")
widgetOne.pack()
widgetTwo = Entry(firstCanvas)
widgetTwo.pack()
widgetThree = Label(secondCanvas, text='Spam')
widgetThree.pack()
widgetFour = Entry(secondCanvas)
widgetFour.pack()

# Configure scrollbar
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Main loop
mainloop()
