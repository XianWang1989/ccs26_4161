
from tkinter import *

def update_scrollregion(event):
    # Update the scrollregion of the first canvas to encompass its content
    firstCanvas.configure(scrollregion=firstCanvas.bbox("all"))

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)
firstCanvas.bind("<Configure>", update_scrollregion)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create content for the first canvas
for i in range(20):
    Label(firstCanvas, text=f'Label {i}').pack()

# Create content for the second canvas
for i in range(20):
    Label(secondCanvas, text=f'Spam {i}').pack()

# Link scrollbar to canvas views
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

mainloop()
