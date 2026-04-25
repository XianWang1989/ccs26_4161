
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas with a defined scroll region
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 200, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create some content in the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Add labels and entries that extend beyond the visible area
for i in range(20):
    widget = Label(firstCanvas, text=f"This is label {i+1}")
    widget.pack()

# Add more content to the second canvas
for i in range(50):
    widget = Label(secondCanvas, text=f"Second Canvas: Item {i+1}")
    widget.pack()

# Configure the scrollbar to scroll the second canvas
scrollbar.config(command=secondCanvas.yview)

# Bind the scrollbar to the second canvas
def on_mouse_wheel(event):
    secondCanvas.yview_scroll(int(-1*(event.delta/120)), "units")

root.bind_all("<MouseWheel>", on_mouse_wheel)

mainloop()
