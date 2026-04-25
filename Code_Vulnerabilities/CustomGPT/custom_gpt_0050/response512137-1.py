
from tkinter import *

# Create the main window
root = Tk()

# Create a vertical scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the scrollbar to scroll both canvases
def on_canvas_scroll(event):
    firstCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
    secondCanvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Create the first canvas with a scrollbar
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=400)
secondCanvas.pack(side="left", fill="both", expand=True)

# Attach scrollbar to second canvas
secondCanvas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=secondCanvas.yview)

# Create content in first canvas
for i in range(20):
    Label(firstCanvas, text=f'Label {i}').pack()

# Create content in second canvas
for i in range(100):
    Label(secondCanvas, text=f'Some content {i}').pack()

# Bind the scrollbar and canvas scrolling
secondCanvas.bind_all("<MouseWheel>", on_canvas_scroll)

# Configure the scrollregion of the second canvas
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

mainloop()
