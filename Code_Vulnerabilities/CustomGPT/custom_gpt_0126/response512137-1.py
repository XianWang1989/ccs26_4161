
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=500)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Link second canvas to scrollbar
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Adding multiple widgets to first canvas for testing
for i in range(20):
    Label(firstCanvas, text=f'This is a test {i}').pack()

# Adding widgets to the second canvas to show content
for i in range(50):
    Label(secondCanvas, text=f'Spam {i}').pack()

# Creating a large rectangle on the second canvas
secondCanvas.create_rectangle(10, 10, 200, 6000, fill='lightgrey')

mainloop()
