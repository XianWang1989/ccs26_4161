
from tkinter import *

root = Tk()

# Create a frame to hold the canvases and scrollbar
frame = Frame(root)
frame.pack()

# Create the first canvas
firstCanvas = Canvas(frame, width=200, height=500)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(frame, width=200, height=500)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a scrollbar
scrollbar = Scrollbar(frame, command=firstCanvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvases to use the scrollbar
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Create a scroll region for the second canvas
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Add widgets to the first canvas
for i in range(20):  # Add many labels
    Label(firstCanvas, text=f"Label {i+1}").pack()

# Add widgets to the second canvas
for i in range(50):  # Add many entries
    Entry(secondCanvas).pack()

# Update the scroll region for the second canvas
secondCanvas.update_idletasks()

# Set the scroll region from the children of secondCanvas
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Run the application
root.mainloop()
