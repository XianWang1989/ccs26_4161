
from tkinter import *

# Create the main window
root = Tk()

# Create scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=500, bg='lightblue')
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Connect the scrollbar to both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Add widgets to the first canvas
widgets = [Label(firstCanvas, text=f"Label {i}") for i in range(30)]
for widget in widgets:
    widget.pack()

# Add widgets to the second canvas
widgets_second = [Label(secondCanvas, text=f"Entry {i}") for i in range(30)]
for widget in widgets_second:
    widget.pack()

# Run the main loop
mainloop()
