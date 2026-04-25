
from tkinter import *

# Create the main window
root = Tk()
root.title("Scrollable Canvases")

# Create scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create frame to hold canvases
frame = Frame(root)
frame.pack(side=LEFT, fill=BOTH, expand=True)

# Create first canvas
firstCanvas = Canvas(frame, width=200, height=400)
firstCanvas.pack(side=LEFT, fill=BOTH, expand=True)

# Create second canvas
secondCanvas = Canvas(frame, width=200, height=400)
secondCanvas.pack(side=LEFT, fill=BOTH, expand=True)

# Configure scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Configure yscroll command for each canvas
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Create a scrollable area for second canvas
secondCanvas.create_rectangle(200, 300, 300, 6000)

# Add widgets to the first canvas
for i in range(30):  # Add multiple labels to test scrolling
    widget = Label(firstCanvas, text=f'This is widget {i+1}')
    firstCanvas.create_window(100, 20 * i, window=widget)

# Add some entries to the second canvas
for i in range(10):  # Add multiple entries to test scrolling
    entry = Entry(secondCanvas)
    secondCanvas.create_window(100, 20 * i, window=entry)

# Set the scroll region for the second canvas
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Start the main loop
mainloop()
