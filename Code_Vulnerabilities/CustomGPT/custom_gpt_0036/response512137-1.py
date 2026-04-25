
from tkinter import *

root = Tk()

# Define the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Define a scrollable region for the first canvas
firstCanvas.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=firstCanvas.yview)

# Add widgets to the first canvas
for i in range(50):  # Adding multiple widgets for scrolling
    widget = Label(firstCanvas, text=f'Label {i+1}')
    firstCanvas.create_window(10, i*25, anchor='nw', window=widget)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=400)
secondCanvas.pack(side="left", fill="both", expand=True)

# Set the scrollregion for the second canvas
secondCanvas.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=secondCanvas.yview)

# Add widgets to the second canvas
for i in range(50):  # Adding multiple widgets for scrolling
    widget = Label(secondCanvas, text=f'Entry {i+1}')
    secondCanvas.create_window(10, i*25, anchor='nw', window=widget)

# Final scroll region definition
firstCanvas.config(scrollregion=firstCanvas.bbox("all"))
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

root.mainloop()
