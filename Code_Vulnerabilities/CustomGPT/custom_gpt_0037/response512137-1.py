
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas with a defined scroll region
secondCanvas = Canvas(root, width=200, height=400)
secondCanvas.pack(side="left", fill="both", expand=True)

secondCanvas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=secondCanvas.yview)

# Create a frame to hold widgets for scrolling
frame1 = Frame(firstCanvas)
frame2 = Frame(secondCanvas)

firstCanvas.create_window((0, 0), window=frame1, anchor='nw')
secondCanvas.create_window((0, 0), window=frame2, anchor='nw')

# Populate the first canvas
for i in range(30):
    Label(frame1, text=f"Label {i+1} in Canvas 1").pack()

# Populate the second canvas
for i in range(50):
    Label(frame2, text=f"Label {i+1} in Canvas 2").pack()

# Update scroll region
frame1.update_idletasks()
frame2.update_idletasks()

firstCanvas.config(scrollregion=firstCanvas.bbox("all"))
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
