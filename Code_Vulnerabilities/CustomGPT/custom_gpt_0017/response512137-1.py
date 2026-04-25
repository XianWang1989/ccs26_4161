
from tkinter import *

root = Tk()

# Create scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure scrollbar to control secondCanvas
scrollbar.config(command=secondCanvas.yview)

# Make canvases scrollable
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Add widgets to the first canvas
for i in range(20):
    label = Label(firstCanvas, text=f"Label {i + 1}")
    label.pack()

# Add widgets to the second canvas
for i in range(50):
    label = Label(secondCanvas, text=f"Spam {i + 1}")
    label.pack()

# Make sure to also set scrollregion for the second canvas
secondCanvas.update_idletasks()  # Update sizes
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
