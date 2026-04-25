
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=5000, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link the scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Add widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Adding additional widgets to both canvases
for i in range(20):  # Adding more widgets for scrolling
    widget = Label(firstCanvas, text=f'This is entry {i + 1}')
    widget.pack()

# Adding more widgets to the second canvas
widgetTwo = Entry(secondCanvas)
widgetTwo.pack()
widgetThree = Label(secondCanvas, text='More content in second canvas')
widgetThree.pack()
# Add more widgets if needed to overflow

mainloop()
