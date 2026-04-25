
from tkinter import *

root = Tk()

# Scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=10000, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Linking both canvases to the scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Adding widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Lots of widgets for scrolling
for text in ["this is a test", "More widgets to scroll", "Even more widgets", "And yet more!"]:
    Label(firstCanvas, text=text).pack()

# Adding widgets to the second canvas
widgetThree = Label(secondCanvas, text='Spam')
widgetThree.pack()

widgetFour = Entry(secondCanvas)
widgetFour.pack()

# Run the application
mainloop()
