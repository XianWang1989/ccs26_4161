
from tkinter import *

root = Tk()

# Create scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Attach scrollbar to second canvas
secondCanvas.config(yscrollcommand=scrollbar.set)

# Create content for the first canvas
for i in range(50):
    widget = Label(firstCanvas, text=f'Item {i+1}')
    firstCanvas.create_window(100, 20*i, window=widget)

# Create content for the second canvas
for i in range(100):
    widget = Label(secondCanvas, text=f'Spam {i+1}')
    secondCanvas.create_window(100, 20*i, window=widget)

# Ensure the second canvas can be scrolled
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
