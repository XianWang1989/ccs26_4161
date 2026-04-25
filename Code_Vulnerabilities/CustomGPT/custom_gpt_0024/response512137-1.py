
from tkinter import *

def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = Tk()

# Create a vertical scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link the scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Add content to the first canvas
for i in range(15):
    widget = Label(firstCanvas, text=f'Label {i}')
    widget.pack()

# Add content to the second canvas
for i in range(50):
    entry = Entry(secondCanvas)
    entry.insert(0, f'Entry {i}')
    entry.pack()

# Update the scroll region of the second canvas
secondCanvas.bind("<Configure>", lambda e: on_frame_configure(secondCanvas))

mainloop()
