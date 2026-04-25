
from tkinter import *

def on_canvas_configure(event):
    firstCanvas.configure(scrollregion=firstCanvas.bbox("all"))
    secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

root = Tk()

# Create scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)
firstFrame = Frame(firstCanvas)
firstCanvas.create_window((0, 0), window=firstFrame, anchor='nw')

# Create second canvas
secondCanvas = Canvas(root, width=200, height=400)
secondCanvas.pack(side="left", fill="both", expand=True)
secondFrame = Frame(secondCanvas)
secondCanvas.create_window((0, 0), window=secondFrame, anchor='nw')

# Configure scrollbar for second canvas
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding widgets to first canvas
for i in range(30):
    Label(firstFrame, text=f"Label {i+1}").pack()

# Adding widgets to second canvas
for i in range(100):
    Label(secondFrame, text=f"Entry {i+1}").pack()

# Configure canvases scrolling
firstCanvas.bind("<Configure>", on_canvas_configure)
secondCanvas.bind("<Configure>", on_canvas_configure)

mainloop()
