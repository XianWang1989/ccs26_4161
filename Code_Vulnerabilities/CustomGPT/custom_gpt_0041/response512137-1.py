
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create a frame to hold both canvases
frame = Frame(root)
frame.pack(side="left", fill="both", expand=True)

# First canvas
firstCanvas = Canvas(frame, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(frame, width=200, height=400, scrollregion=(0, 0, 200, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbar to second canvas
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding content to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Adding lots of widgets to the second canvas
for i in range(100):
    Label(secondCanvas, text=f'This is a test {i}').pack()

# Ensure the scrolling region is set for second canvas
secondCanvas.update_idletasks()  # Update canvas sizes
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
