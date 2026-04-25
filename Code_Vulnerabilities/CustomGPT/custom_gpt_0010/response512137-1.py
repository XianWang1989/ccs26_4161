
from tkinter import *

root = Tk()

# Create scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Linking scrollbar with the second canvas
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding content to the first canvas
for i in range(15):
    Label(firstCanvas, text=f"Label {i + 1}").pack()

# Adding content to the second canvas
for i in range(50):
    Label(secondCanvas, text=f"Second Canvas Label {i + 1}").pack()

# Create an extra rectangle in the second canvas
secondCanvas.create_rectangle(0, 0, 200, 5000, outline="black")

mainloop()
