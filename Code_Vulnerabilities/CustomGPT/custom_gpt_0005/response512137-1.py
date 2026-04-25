
from tkinter import *

root = Tk()

# Create two frames to hold the canvases
frame1 = Frame(root)
frame1.pack(side=LEFT, fill=BOTH, expand=True)

frame2 = Frame(root)
frame2.pack(side=LEFT, fill=BOTH, expand=True)

# Scrollbar setup
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(frame1, width=200, height=400)
firstCanvas.pack(side=LEFT, fill=BOTH, expand=True)

# Second Canvas
secondCanvas = Canvas(frame2, width=200, height=400, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side=LEFT, fill=BOTH, expand=True)

# Connecting canvases to scrollbar
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding widgets to the first canvas
for i in range(20):
    widget = Label(firstCanvas, text=f'This is label {i+1}')
    firstCanvas.create_window(100, i * 20, window=widget)

# Adding widgets to the second canvas
for i in range(250):
    widget = Label(secondCanvas, text=f'This is label {i+1}')
    secondCanvas.create_window(100, i * 20, window=widget)

# Main loop
mainloop()
