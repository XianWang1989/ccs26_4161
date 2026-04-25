
from tkinter import *

root = Tk()

# Create first canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(root, width=200, height=300)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a scrollbar
scrollbar = Scrollbar(root, orient="vertical", command=firstCanvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvases to use the scrollbar
firstCanvas.configure(yscrollcommand=scrollbar.set)
secondCanvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to hold the widgets in each canvas
frame1 = Frame(firstCanvas)
frame2 = Frame(secondCanvas)

# Add content to the first canvas
for i in range(20):
    Label(frame1, text=f'Label {i}').pack()

# Add content to the second canvas
for i in range(20, 40):
    Label(frame2, text=f'Label {i}').pack()

# Create window for the first canvas
firstCanvas.create_window(0, 0, window=frame1, anchor='nw')
firstCanvas.update_idletasks()

# Create window for the second canvas
secondCanvas.create_window(0, 0, window=frame2, anchor='nw')
secondCanvas.update_idletasks()

# Set the scroll region for both canvases
firstCanvas.config(scrollregion=firstCanvas.bbox("all"))
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
