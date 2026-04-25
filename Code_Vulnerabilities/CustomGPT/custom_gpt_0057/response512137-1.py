
from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Populate the first canvas
for i in range(30):
    widget = Label(firstCanvas, text=f'This is label {i}')
    widget.pack()

# Populate the second canvas
for i in range(50):
    widget = Label(secondCanvas, text=f'Second canvas label {i}')
    widget.pack()

mainloop()
