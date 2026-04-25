
from tkinter import *

root = Tk()

# Create two canvases
firstCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 200, 1000))
firstCanvas.pack(side="left", fill="both", expand=True)

secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 200, 1000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a scrollbar
scrollbar = Scrollbar(root, command=secondCanvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the second canvas to use the scrollbar
secondCanvas.config(yscrollcommand=scrollbar.set)

# Create widgets in the first canvas
for i in range(30):  # Add multiple widgets to ensure scrolling
    Label(firstCanvas, text=f'This is label {i}').pack()

# Create widgets in the second canvas
for i in range(50):  # Add multiple widgets to ensure scrolling
    Label(secondCanvas, text=f'This is label {i} in second canvas').pack()

# A rectangle in the second canvas for visibility
secondCanvas.create_rectangle(50, 50, 150, 450, fill='blue')

# Start the main loop
root.mainloop()
