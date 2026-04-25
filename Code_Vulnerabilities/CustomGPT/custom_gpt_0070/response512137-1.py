
from tkinter import *

root = Tk()

# Create scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 200, 800))
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbars
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Add content to the first canvas
for i in range(20):
    widget = Label(firstCanvas, text=f'Spam {i + 1}')
    widget.pack()

# Add content to the second canvas
for i in range(30):
    widget = Label(secondCanvas, text=f'Test {i + 1}')
    widget.pack()

mainloop()
