
from tkinter import *

# Initialize the main application window
root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 1000))
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a vertical scrollbar to control both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Adding content to the first canvas
for i in range(30):
    widget = Label(firstCanvas, text=f'This is item {i + 1}')
    firstCanvas.create_window(100, i * 30, window=widget)

# Adding content to the second canvas
for i in range(100):
    widget = Label(secondCanvas, text=f'Spam {i + 1}')
    secondCanvas.create_window(100, i * 30, window=widget)

# Set the scrollregion for the first canvas
firstCanvas.config(scrollregion=firstCanvas.bbox("all"))

# Start the main loop
mainloop()
