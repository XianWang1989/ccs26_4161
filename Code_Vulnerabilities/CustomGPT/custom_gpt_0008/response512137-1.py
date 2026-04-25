
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure scrollbar
scrollbar.config(command=secondCanvas.yview)

# Add widgets to first canvas
firstCanvas.create_window(100, 50, window=Label(firstCanvas, text='Spam'))
for i in range(20):
    Label(firstCanvas, text=f"Item {i}").pack()

# Add widgets to second canvas
for i in range(100):
    Label(secondCanvas, text=f"Label {i}").pack()

# Making sure to update the scrollregion after adding the widgets
secondCanvas.update_idletasks()
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
