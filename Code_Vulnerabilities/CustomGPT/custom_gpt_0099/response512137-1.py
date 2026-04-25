
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create canvas to hold both scrollable content
canvas = Canvas(root, width=400, height=400)
canvas.pack(side="left", fill="both", expand=True)

# Create a frame inside the canvas
frame = Frame(canvas)

# Configure the scrollbar
scrollbar.config(command=canvas.yview)

# Add the frame to the canvas
canvas.create_window((0, 0), window=frame, anchor='nw')

# Bind the configuration of the canvas scrolling region to the frame
def configure_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

frame.bind("<Configure>", configure_scrollregion)

# Add widgets to the frame
widget = Label(frame, text='Spam')
widget.pack()

# Lots of widgets to ensure scrolling
for i in range(20):
    widget = Label(frame, text=f"This is label {i}")
    widget.pack()

# Main loop
mainloop()
