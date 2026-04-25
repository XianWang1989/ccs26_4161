
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Frame to hold canvases
frame = Frame(root)
frame.pack(side="left", fill="both", expand=True)

# First Canvas
firstCanvas = Canvas(frame, width=200, height=500)
firstCanvas.pack(side="top", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(frame, width=200, height=500)
secondCanvas.pack(side="top", fill="both", expand=True)

# Configure scrollbar
secondCanvas.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=secondCanvas.yview)

# Create a scroll region for the second canvas
secondCanvas.config(scrollregion=(0, 0, 200, 1500))  # Adjusted scroll region

# Adding widgets to first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Adding multiple widgets to second canvas
for i in range(20):
    Label(secondCanvas, text=f'This is test label {i}').pack()

# Finalizing layout
firstCanvas.create_window((0, 0), window=firstCanvas)
secondCanvas.create_window((0, 0), window=secondCanvas)

mainloop()
