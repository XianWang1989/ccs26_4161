
from tkinter import *

# Create the main application window
root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=500)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas with a defined scroll region
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Link the scrollbar to the yview of both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Scroll commands for both canvases
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Add some widgets to the first canvas
for i in range(20):
    label = Label(firstCanvas, text=f'This is item {i}')
    label.pack()

# Add some widgets to the second canvas
for i in range(50):
    label = Label(secondCanvas, text=f'Spam {i}')
    label.pack()

# Start the main event loop
root.mainloop()
