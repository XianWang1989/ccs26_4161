
from tkinter import *

def on_scroll(*args):
    firstCanvas.yview(*args)
    secondCanvas.yview(*args)

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

secondCanvas = Canvas(root, width=200, height=5000, scrollregion=(0,0,0,5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Assuming you want to bind scrolling functionality to the scrollbar
scrollbar.config(command=on_scroll)

# Example widgets
for i in range(30):
    widget = Label(firstCanvas, text=f'This is label {i}')
    widget.pack()

for i in range(50):
    widget = Label(secondCanvas, text=f'Second Canvas Label {i}')
    widget.pack()

mainloop()
