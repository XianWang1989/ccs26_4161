
from tkinter import *

def on_canvas_configure(event):
    # Update the scrollregion of the canvas to encompass the inner frame
    canvas1.configure(scrollregion=canvas1.bbox("all"))
    canvas2.configure(scrollregion=canvas2.bbox("all"))

# Create the main window
root = Tk()

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create two canvases
canvas1 = Canvas(root, width=200, height=400)
canvas1.pack(side="left", fill="both", expand=True)
canvas2 = Canvas(root, width=200, height=400)
canvas2.pack(side="left", fill="both", expand=True)

# Link the scrollbar to both canvases
scrollbar.config(command=lambda *args: (canvas1.yview(*args), canvas2.yview(*args)))

# Add content to the first canvas
frame1 = Frame(canvas1)
canvas1.create_window((0, 0), window=frame1, anchor='nw')

for i in range(50):
    Label(frame1, text=f"Label {i+1}").pack()

# Add content to the second canvas
frame2 = Frame(canvas2)
canvas2.create_window((0, 0), window=frame2, anchor='nw')

for i in range(100):
    Label(frame2, text=f"Entry {i+1}").pack()

# Configure the canvas to update the scrollregion
canvas1.bind("<Configure>", on_canvas_configure)
canvas2.bind("<Configure>", on_canvas_configure)

# Run the application
mainloop()
