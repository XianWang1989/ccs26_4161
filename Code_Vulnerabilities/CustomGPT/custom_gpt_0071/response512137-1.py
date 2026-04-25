
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 1000))
firstCanvas.pack(side="left", fill="both", expand=True)
firstCanvas.create_window((0, 0), window=Frame(firstCanvas), anchor="nw")
frame1 = Frame(firstCanvas)
firstCanvas.create_window((0, 0), window=frame1, anchor='nw')

# Second Canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)
secondCanvas.create_window((0, 0), window=Frame(secondCanvas), anchor="nw")
frame2 = Frame(secondCanvas)
secondCanvas.create_window((0, 0), window=frame2, anchor='nw')

# Adding widgets to first canvas
Label(frame1, text='Spam').pack()
for i in range(20):
    Label(frame1, text=f"Label {i}").pack()

# Adding widgets to second canvas
for i in range(50):
    Label(frame2, text=f"Spam {i}").pack()

# Configure scrollbar to scroll both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

mainloop()
