
from tkinter import *

root = Tk()

# Create scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(root, width=200, height=10000)
secondCanvas.pack(side="left", fill="both", expand=True)

# Update scroll region based on content
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Add widgets to first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Adding more widgets
for i in range(50):
    Label(firstCanvas, text=f"Label {i}").pack()

# Add widgets to second canvas
for i in range(100):
    Label(secondCanvas, text=f"Label {i}").pack()

# Link scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

mainloop()
