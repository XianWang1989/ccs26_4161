
from tkinter import *

def on_mouse_wheel(event):
    # Scroll the canvas using mouse wheel
    secondCanvas.yview_scroll(int(-1*(event.delta/120)), "units")

root = Tk()

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a rectangle in the second canvas
secondCanvas.create_rectangle((50, 50, 150, 2500), fill='grey')

# Create widgets in the first canvas
for i in range(40):
    widget = Label(firstCanvas, text='Spam {}'.format(i))
    widget.pack()

# Create widgets in the second canvas
for i in range(20):
    widget = Label(secondCanvas, text='Spam {}'.format(i))
    widget.pack()

# Configure the scrollbar to control the second canvas
scrollbar.config(command=secondCanvas.yview)

# Bind mouse wheel event (for Windows)
root.bind_all("<MouseWheel>", on_mouse_wheel)

mainloop()
