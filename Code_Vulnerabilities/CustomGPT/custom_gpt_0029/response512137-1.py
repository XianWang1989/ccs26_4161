
from tkinter import *

root = Tk()

# Creating the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Creating a frame to hold both canvases
frame = Frame(root)
frame.pack(side=LEFT, fill=BOTH, expand=True)

# Creating the first canvas
firstCanvas = Canvas(frame, width=200, height=100)
firstCanvas.pack(side=TOP, fill=BOTH, expand=True)

# Creating the second canvas
secondCanvas = Canvas(frame, width=200, height=1000, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side=TOP, fill=BOTH, expand=True)

# Configuring the scrollbar to scroll the second canvas
scrollbar.config(command=secondCanvas.yview)

# Adding widgets to the first canvas
widgetOne = Label(firstCanvas, text="This is a test")
widgetOne.pack()
widgetTwo = Entry(firstCanvas)
widgetTwo.pack()
widgetThree = Label(firstCanvas, text='Spam')
widgetThree.pack()

# Adding lots of widgets to the second canvas
for i in range(30):
    Label(secondCanvas, text=f'Entry {i+1}').pack()

# Allow the scrollbar to control the secondCanvas
secondCanvas.update_idletasks()  # Update the scrollregion
mainloop()
