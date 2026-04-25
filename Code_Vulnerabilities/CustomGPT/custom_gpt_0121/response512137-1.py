
from tkinter import *

# Create the root window
root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Frame to hold the canvases
frame = Frame(root)
frame.pack(side=LEFT, fill=BOTH, expand=True)

# First canvas
firstCanvas = Canvas(frame, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(frame, width=200, height=300)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure scrollbar
scrollbar.config(command=firstCanvas.yview)

# Create a frame inside the first canvas to hold widgets
first_frame = Frame(firstCanvas)
firstCanvas.create_window((0, 0), window=first_frame, anchor='nw')

# Create a frame inside the second canvas to hold widgets
second_frame = Frame(secondCanvas)
secondCanvas.create_window((0, 0), window=second_frame, anchor='nw')

# Add widgets to the first canvas
for i in range(30):
    Label(first_frame, text=f'This is label {i}').pack()

# Add widgets to the second canvas
for i in range(30):
    Label(second_frame, text=f'Spam {i}').pack()

# Update scrollregion after adding widgets
first_frame.update_idletasks()
firstCanvas.config(scrollregion=firstCanvas.bbox("all"))
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

# Sync scrollbars
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Main loop
mainloop()
