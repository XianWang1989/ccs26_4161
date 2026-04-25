
from tkinter import *

root = Tk()

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create two canvases
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

secondCanvas = Canvas(root, width=200, height=400)
secondCanvas.pack(side="left", fill="both", expand=True)

# Set the scroll region for the second canvas
secondCanvas.config(scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)

# Configure the scrollbar
scrollbar.config(command=secondCanvas.yview)

# Add widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

for i in range(30):  # Add multiple labels to ensure scrolling
    Label(firstCanvas, text=f'Label {i}').pack()

# Add widgets to the second canvas
for i in range(30):  # Add multiple widgets for testing
    Label(secondCanvas, text=f'Spam {i}').pack()
    Entry(secondCanvas).pack()

# Main loop
root.mainloop()
