
from tkinter import *

root = Tk()

# Create a frame to hold the canvases and scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=TRUE)

# Create the scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create a canvas for the first section
firstCanvas = Canvas(frame, height=400, width=200)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create a canvas for the second section
secondCanvas = Canvas(frame, height=400, width=200)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure the scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Create a scrolling region for the second canvas
secondCanvas.config(scrollregion=(0, 0, 0, 5000))

# Add content to the first canvas
widget = Label(firstCanvas, text='Spam - First Canvas')
widget.pack()
for i in range(50):  # Adding multiple widgets to ensure scrolling
    Label(firstCanvas, text=f"Label {i+1}").pack()

# Add content to the second canvas
for i in range(50, 100):  # Adding multiple widgets to ensure scrolling
    Label(secondCanvas, text=f"Label {i+1}").pack()

# Set the yscroll command for the second canvas
secondCanvas.config(yscrollcommand=scrollbar.set)

# Start the main loop
mainloop()
