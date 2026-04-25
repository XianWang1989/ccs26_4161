
from tkinter import *

def configure_scrollregion(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link canvas to scrollbar
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Add widgets to the first canvas
for i in range(20):
    label = Label(firstCanvas, text=f'This is label {i+1}')
    label.pack()

# Add widgets to the second canvas
for i in range(20):
    entry = Entry(secondCanvas)
    entry.pack()

# Update scrollregion for both canvases
configure_scrollregion(firstCanvas)
configure_scrollregion(secondCanvas)

mainloop()
