
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

# Configure scrollbar
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding widgets to the first canvas
for i in range(20):
    widget = Label(firstCanvas, text=f'This is label {i}')
    widget.pack()

# Adding widgets to the second canvas
for i in range(40):
    widget = Label(secondCanvas, text=f'Spam {i}')
    widget.pack()

# Main loop
mainloop()
