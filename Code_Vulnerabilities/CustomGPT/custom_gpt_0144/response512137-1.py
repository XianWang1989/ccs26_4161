from tkinter import *

# Initialize the root window
root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas (for the first set of widgets)
firstCanvas = Canvas(root, width=200, height=100, yscrollcommand=scrollbar.set)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas (for the second set of widgets)
secondCanvas = Canvas(root, width=2000, height=1000, scrollregion=(0, 0, 2000, 10000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a rectangle in the second canvas (just as an example)
secondCanvas.create_rectangle(200, 300, 300, 6000)

# Create widgets on the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

widgetOne = Label(firstCanvas, text="This is a test")
widgetOne.pack()

widgetTwo = Entry(firstCanvas)
widgetTwo.pack()

# Create widgets on the second canvas
widgetThree = Label(secondCanvas, text='Spam')
widgetThree.pack()

widgetFour = Entry(secondCanvas)
widgetFour.pack()

# Link the scrollbar to both canvases' yview commands
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Run the Tkinter event loop
mainloop()
