
from tkinter import *

root = Tk()

# Create Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first Canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second Canvas with a larger scrolling area
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Add items to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

widgetOne = Label(firstCanvas, text="this is a test")
widgetOne.pack()

# Add a few more widgets to simulate scrolling
for i in range(15):
    Label(firstCanvas, text=f"Label {i}").pack()

# Add items to the second canvas
secondCanvas.create_rectangle(200, 300, 300, 600)
widgetThree = Label(secondCanvas, text='Spam in second canvas')
widgetThree.pack()

for i in range(50):
    Entry(secondCanvas).pack()

# Configure the scrollbar to scroll the second canvas
scrollbar.config(command=secondCanvas.yview)

# Bind scrolling to the canvas
def on_canvas_scroll(event):
    secondCanvas.yview_scroll(int(-1*(event.delta/120)), "units")

secondCanvas.bind_all("<MouseWheel>", on_canvas_scroll)

mainloop()
