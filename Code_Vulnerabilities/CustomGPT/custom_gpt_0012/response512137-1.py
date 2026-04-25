
from tkinter import *

root = Tk()

# Create frames to hold the canvases and scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=TRUE)

# Create the first canvas
firstCanvas = Canvas(frame, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(frame, width=200, height=10000)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create scrollbar
scrollbar = Scrollbar(frame, orient=VERTICAL, command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))
scrollbar.pack(side=RIGHT, fill=Y)

# Configure canvases to use the scrollbar
firstCanvas.configure(yscrollcommand=scrollbar.set)
secondCanvas.configure(yscrollcommand=scrollbar.set)

# Create a scrollregion for the second canvas (must match content size)
secondCanvas.config(scrollregion=(0, 0, 200, 5000))

# Add widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Lots of widgets for the first canvas
for i in range(15):
    widgetOne = Label(firstCanvas, text=f"This is a test {i+1}")
    widgetOne.pack()

# Add widgets to the second canvas
for i in range(30):
    widgetTwo = Entry(secondCanvas)
    widgetTwo.pack()

# Create a rectangle on the second canvas
secondCanvas.create_rectangle((200, 300, 300, 6000))

mainloop()
