
from tkinter import *

# Create the main application window
root = Tk()
root.geometry("400x400")  # Set a window size

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 200, 500), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create content for the first canvas
for i in range(20):
    Label(firstCanvas, text=f"Label {i+1}").pack()

# Create content for the second canvas
for i in range(30):
    Label(secondCanvas, text=f"Label {i+1} in second canvas").pack()

# Link the scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Run the application
mainloop()
