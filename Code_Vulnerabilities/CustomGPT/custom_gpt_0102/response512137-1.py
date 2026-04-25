
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link the scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Add widgets to the first canvas
for i in range(15):  # Add multiple widgets
    widget = Label(firstCanvas, text=f'This is label {i + 1}')
    widget.pack()

# Add widgets to the second canvas
for i in range(40):  # More widgets to create the scroll effect
    widget = Label(secondCanvas, text=f'Spam {i + 1}')
    widget.pack()

# Define a larger scroll region for the second canvas
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

mainloop()
