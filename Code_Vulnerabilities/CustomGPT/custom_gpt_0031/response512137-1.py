
from tkinter import *

def on_canvas_scroll(event):
    # Scroll the second canvas when the scrollbar is moved
    secondCanvas.yview_scroll(int(-1*(event.delta/120)), "units")

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas with a scroll region
secondCanvas = Canvas(root, width=200, height=5000, scrollregion=(0, 0, 200, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link the scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Add content to the first canvas
Label(firstCanvas, text='Spam').pack()
Label(firstCanvas, text="This is a test").pack()
Entry(firstCanvas).pack()
Label(secondCanvas, text='Spam').pack()
Entry(secondCanvas).pack()

# Bind the scrollbar to allow scrolling using the mouse wheel
secondCanvas.bind_all("<MouseWheel>", on_canvas_scroll)

mainloop()
