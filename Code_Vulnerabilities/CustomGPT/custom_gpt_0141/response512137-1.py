
from tkinter import *

# Create the root window
root = Tk()

# Create a vertical scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=300)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a frame in the first canvas to hold widgets
frame_first = Frame(firstCanvas)
firstCanvas.create_window((0, 0), window=frame_first, anchor='nw')

# Create a frame in the second canvas to hold widgets
frame_second = Frame(secondCanvas)
secondCanvas.create_window((0, 0), window=frame_second, anchor='nw')

# Add widgets to the first canvas
for i in range(30):  # Example of adding multiple labels
    Label(frame_first, text=f"Label {i}").pack()

# Add widgets to the second canvas
for i in range(100):  # Example of adding multiple entries
    Entry(frame_second).pack()

# Update scrollregion to encompass the content on both canvases
def update_scrollregion(event):
    firstCanvas.configure(scrollregion=firstCanvas.bbox("all"))
    secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Configure the scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Bind the first canvas to scrollbar
firstCanvas.bind('<Configure>', update_scrollregion)
secondCanvas.bind('<Configure>', update_scrollregion)

# Configure the canvases to scroll together
firstCanvas.configure(yscrollcommand=scrollbar.set)
secondCanvas.configure(yscrollcommand=scrollbar.set)

# Start the GUI event loop
mainloop()
