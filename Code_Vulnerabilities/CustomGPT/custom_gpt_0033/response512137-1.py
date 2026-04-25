
from tkinter import *

# Initialize the main application window
root = Tk()

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create two canvases
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 600))
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure scrollbar to control both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Create content for the first canvas
for i in range(20):  # Example with multiple widgets
    Label(firstCanvas, text=f"Label {i}").pack()

# Create content for the second canvas
for i in range(30):  # Example with more widgets
    Label(secondCanvas, text=f"Second Canvas - Label {i}").pack()

# Update scroll region to fit the content
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Set the scroll region based on the number of widgets
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

# Run the main event loop
mainloop()
