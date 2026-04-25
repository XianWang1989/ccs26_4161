
from tkinter import *

root = Tk()
root.geometry("400x300")  # Set a window size

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Create a frame for the first canvas to hold widgets
frame1 = Frame(firstCanvas)
firstCanvas.create_window((0, 0), window=frame1, anchor='nw')

# Create a frame for the second canvas to hold widgets
frame2 = Frame(secondCanvas)
secondCanvas.create_window((0, 0), window=frame2, anchor='nw')

# Add widgets to the first frame
for i in range(20):  # Example labels in frame1
    Label(frame1, text=f"Label {i}").pack()

# Add widgets to the second frame
for i in range(100):  # Example labels in frame2
    Label(frame2, text=f"Label {i}").pack()

# Command the scrollbar to control both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Update scrollregion of second canvas
secondCanvas.update_idletasks()
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
