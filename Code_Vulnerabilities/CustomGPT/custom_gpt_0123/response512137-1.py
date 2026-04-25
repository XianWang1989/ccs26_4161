
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas with larger content
secondCanvas = Canvas(root, width=200, height=400)
secondCanvas.pack(side="left", fill="both", expand=True)

# Set the scroll region for the second canvas
secondCanvas.configure(scrollregion=(0, 0, 0, 5000))
secondCanvas.config(yscrollcommand=scrollbar.set)

# Create some widgets for the first canvas
for i in range(15):
    widget = Label(firstCanvas, text=f'Label {i+1}')
    widget.pack()

# Create some widgets for the second canvas
for i in range(30):
    widget = Label(secondCanvas, text=f'Spam {i+1}')
    widget.pack()

# Configure scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

mainloop()
