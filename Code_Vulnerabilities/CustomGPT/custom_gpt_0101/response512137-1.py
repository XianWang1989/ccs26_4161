
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a rectangle on the second canvas
secondCanvas.create_rectangle((200, 300, 300, 6000))

# Widgets for the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Additional widgets
for i in range(20):
    Label(firstCanvas, text=f"This is a test {i+1}").pack()

# Widgets for the second canvas
Label(secondCanvas, text='Spam').pack()
Entry(secondCanvas).pack()

# Configure scrollbar
scrollbar.config(command=secondCanvas.yview)

mainloop()
