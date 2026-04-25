
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Frame to hold both canvases
frame = Frame(root)
frame.pack(side="left", fill="both", expand=True)

# First canvas
firstCanvas = Canvas(frame, width=200, height=100)
firstCanvas.pack(side="top", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(frame, width=200, height=10000,scrollregion=(0,0,0,5000),yscrollcommand=scrollbar.set)
secondCanvas.pack(side="top", fill="both", expand=True)

# Adding widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

widgetOne=Label(firstCanvas, text="This is a test")
widgetOne.pack()
widgetTwo=Entry(firstCanvas)
widgetTwo.pack()
widgetThree=Label(secondCanvas, text='Spam')
widgetThree.pack()

# Adding more widgets to ensure scrolling is visible
for i in range(50):
    Label(secondCanvas, text=f"Label {i}").pack()

# Configuring the scrollbar
scrollbar.config(command=secondCanvas.yview)

mainloop()
