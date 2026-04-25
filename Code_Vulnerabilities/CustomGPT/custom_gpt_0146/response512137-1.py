
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=300)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure scroll region for second canvas
secondCanvas.configure(scrollregion=(0, 0, 0, 5000))

# Set yscrollcommand for scrollbar
secondCanvas.config(yscrollcommand=scrollbar.set)

# Create lots of widgets in first and second canvas for demo purposes
for i in range(20):
    Label(firstCanvas, text=f"Label {i + 1}").pack()

for i in range(50):
    Label(secondCanvas, text=f"Spam {i + 1}").pack()

# Scrollbar command
scrollbar.config(command=secondCanvas.yview)

mainloop()
