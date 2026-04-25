
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0,0,0,5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Linking scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Create a frame inside the second canvas to contain content
frame = Frame(secondCanvas)
secondCanvas.create_window((0, 0), window=frame, anchor='nw')

# Populate first canvas
Label(firstCanvas, text='Spam').pack()
Label(firstCanvas, text="This is a test").pack()
Entry(firstCanvas).pack()

# Populate second canvas
for i in range(50):
    Label(frame, text=f'Label {i}').pack()

# Update the scrollregion of the second canvas to match the frame size
frame.update_idletasks()
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
