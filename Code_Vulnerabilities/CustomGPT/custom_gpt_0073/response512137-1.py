
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configuring the scrollbar
scrollbar.config(command=secondCanvas.yview)

# Adding widgets to first Canvas
for i in range(20):
    widget = Label(firstCanvas, text=f'This is label {i}')
    widget.pack()

# Adding widgets to second Canvas
for i in range(50):
    widget = Label(secondCanvas, text=f'Spam {i}')
    widget.pack()

# Create a rectangle in the second canvas
secondCanvas.create_rectangle((0, 0, 200, 5000), outline="blue")  # Adjust as necessary

# Start the main event loop
mainloop()
