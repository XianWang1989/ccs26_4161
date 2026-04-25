
from tkinter import *

root = Tk()

# Create the scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 1500))
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 1500), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbar to both canvases
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Add widgets to the first canvas
for i in range(30):
    Label(firstCanvas, text=f'Label {i+1}').pack()

# Add widgets to the second canvas
for i in range(30):
    Entry(secondCanvas).pack()

mainloop()
