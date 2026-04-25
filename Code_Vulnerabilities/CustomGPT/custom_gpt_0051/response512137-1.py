
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=300, bg='lightblue')
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=300, bg='lightgreen')
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure the scroll region for the second canvas
secondCanvas.configure(scrollregion=(0, 0, 0, 500))

# Create content for the first canvas
for i in range(10):
    Label(firstCanvas, text=f'Label {i}').pack()

# Create content for the second canvas
for i in range(20):
    Label(secondCanvas, text=f'Entry {i}').pack()

# Configure scrollbar
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Update the scrollregion when widgets are added
secondCanvas.update_idletasks()
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

mainloop()
