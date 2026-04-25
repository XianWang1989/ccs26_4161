
from tkinter import *

# Create the main window
root = Tk()

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=500, scrollregion=(0,0,0,1000))
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0,0,0,10000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure the scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Add widgets to the first canvas
for i in range(30):  # example to add multiple widgets
    Label(firstCanvas, text=f"Label {i}").pack()

# Add widgets to the second canvas
for i in range(30, 60):  # example to add multiple widgets
    Label(secondCanvas, text=f"Label {i}").pack()

# Start the main event loop
mainloop()
