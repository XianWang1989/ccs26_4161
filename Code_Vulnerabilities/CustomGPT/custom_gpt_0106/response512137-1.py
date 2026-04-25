
from tkinter import *

root = Tk()

# Scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Frame to hold the canvases
frame = Frame(root)
frame.pack(side="left", fill="both", expand=True)

# First canvas
firstCanvas = Canvas(frame, width=200, height=400)
firstCanvas.pack(side="top", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(frame, width=200, height=400, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="top", fill="both", expand=True)

# Linking scrollbar to both canvases
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Adding content to the first canvas
for i in range(20):
    Label(firstCanvas, text=f'Label {i+1}').pack()

# Adding content to the second canvas
for i in range(50):
    Label(secondCanvas, text=f'Spam {i+1}').pack()

# Configuring the scrollbar
firstCanvas.configure(yscrollcommand=scrollbar.set)
secondCanvas.configure(yscrollcommand=scrollbar.set)

mainloop()
