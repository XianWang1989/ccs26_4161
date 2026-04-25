
from tkinter import *

def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = Tk()

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the main canvas
canvas = Canvas(root, width=400, height=300, yscrollcommand=scrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Link the scrollbar to the canvas
scrollbar.config(command=canvas.yview)

# Create a frame inside the canvas to hold the widgets
frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

# Add widgets to the frame
for i in range(50):  # Example of multiple widgets
    Label(frame, text=f"Label {i+1}").pack()
    Entry(frame).pack()

# Update the scroll region
frame.bind("<Configure>", lambda e: on_frame_configure(canvas))

mainloop()
