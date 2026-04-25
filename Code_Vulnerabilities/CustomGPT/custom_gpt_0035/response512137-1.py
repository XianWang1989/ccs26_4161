
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=500)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 3000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link the scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Add widgets to the first canvas
for i in range(30):
    Label(firstCanvas, text=f"Label {i+1}").pack()

# Add widgets to the second canvas
for i in range(50):
    Label(secondCanvas, text=f"Entry {i+1}").pack()

# Create a rectangle to visualize the second canvas
secondCanvas.create_rectangle(50, 50, 150, 800, outline="black")

mainloop()
