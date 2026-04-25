
from tkinter import *

# Create the main window
root = Tk()

# Create a vertical scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create a frame to hold both canvases
frame = Frame(root)
frame.pack(fill=BOTH, expand=TRUE)

# First Canvas
firstCanvas = Canvas(frame, width=200, height=400)
firstCanvas.pack(side="left", fill=BOTH, expand=True)

# Second Canvas
secondCanvas = Canvas(frame, width=200, height=400)
secondCanvas.pack(side="left", fill=BOTH, expand=True)

# Configure the scrollbar
secondCanvas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=secondCanvas.yview)

# Create a scrollable region in secondCanvas
secondCanvas.configure(scrollregion=(0, 0, 0, 5000))

# Add widgets to the first canvas
Label(firstCanvas, text='Spam').pack()
Label(firstCanvas, text="this is a test").pack()
Entry(firstCanvas).pack()
Entry(firstCanvas).pack()

# Add lots of widgets to the second canvas for scrolling
for i in range(50):
    Label(secondCanvas, text=f'Spam {i}').pack()

# Run the main event loop
mainloop()
