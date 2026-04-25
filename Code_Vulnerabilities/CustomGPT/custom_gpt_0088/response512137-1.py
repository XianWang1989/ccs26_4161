
from tkinter import *

# Create the main window
root = Tk()

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=300)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure the scrollbar to control the second canvas
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Create labels in the first canvas
for i in range(30):
    Label(firstCanvas, text=f"Label {i+1}").pack()

# Create multiple widgets in the second canvas
for i in range(50):
    Label(secondCanvas, text=f"Item {i+1}").pack()

# Set the scroll region for secondCanvas
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

# Keep the main loop running
mainloop()
