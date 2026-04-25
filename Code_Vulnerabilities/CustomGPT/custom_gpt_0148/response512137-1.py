
from tkinter import *

root = Tk()

# Create scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=600)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=200, height=600, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link the scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Adding widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Lots of widgets in first canvas
for i in range(20):
    Label(firstCanvas, text=f'This is label {i+1}').pack()

# Adding widgets to the second canvas
for i in range(50):
    Label(secondCanvas, text=f'This is second canvas label {i+1}').pack()

mainloop()
