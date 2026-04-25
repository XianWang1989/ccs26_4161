
from tkinter import *

# Create the main application window
root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=500)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a rectangle in the second canvas
secondCanvas.create_rectangle((200, 300, 300, 6000))

# Add widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Add more widgets to the first canvas
for i in range(30):  # example to create multiple widgets
    Label(firstCanvas, text=f'This is test label {i}').pack()

# Add widgets to the second canvas
for i in range(30):
    Entry(secondCanvas).pack()

# Configure scrollbar to control both canvases
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Main loop
mainloop()
