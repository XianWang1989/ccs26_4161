
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)
firstCanvas.config(yscrollcommand=scrollbar.set)

# Second canvas
secondCanvas = Canvas(root, width=200, height=300)
secondCanvas.pack(side="left", fill="both", expand=True)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Create a frame to hold the first canvas content
first_frame = Frame(firstCanvas)
firstCanvas.create_window((0, 0), window=first_frame, anchor='nw')

# Create a frame to hold the second canvas content
second_frame = Frame(secondCanvas)
secondCanvas.create_window((0, 0), window=second_frame, anchor='nw')

# Lots of widgets for the first canvas
for i in range(15):
    label = Label(first_frame, text=f"Label {i+1}")
    label.pack()

# Lots of widgets for the second canvas
for i in range(50):
    entry = Entry(second_frame)
    entry.pack()

# Configure scroll region
first_frame.update_idletasks()  # Update to get the correct height
second_frame.update_idletasks()  # Update to get the correct height
firstCanvas.config(scrollregion=firstCanvas.bbox("all"))
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

# Configure scrolling
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

mainloop()
