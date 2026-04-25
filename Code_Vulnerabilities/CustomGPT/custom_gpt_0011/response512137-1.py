
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas and link it to the scrollbar
firstCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 1000))
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas and link it to the scrollbar
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create some widgets in the first canvas
Label(firstCanvas, text='Spam').pack()
for i in range(20):
    Label(firstCanvas, text=f"Label {i+1}").pack()

# Create some widgets in the second canvas
for i in range(50):
    Label(secondCanvas, text=f"Entry {i+1}").pack()

# Configure the scrollbar to command the second canvas
scrollbar.config(command=secondCanvas.yview)

mainloop()
