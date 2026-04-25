
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=5000, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Adding content to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Lots of widgets to extend the scrollable area
for i in range(20):
    widget = Label(firstCanvas, text=f"This is label {i + 1}")
    widget.pack()

# Adding content to the second canvas
widgetThree = Label(secondCanvas, text='Spam in second canvas')
widgetThree.pack()
widgetFour = Entry(secondCanvas)
widgetFour.pack()

# Configuring the scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

mainloop()
