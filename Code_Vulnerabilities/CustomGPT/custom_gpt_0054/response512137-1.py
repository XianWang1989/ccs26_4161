
from tkinter import *

root = Tk()

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure scrollbar for the second canvas
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Add widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Add lots of widgets to the second canvas
for i in range(10):
    Label(secondCanvas, text=f"Label {i+1}").pack()

# Adding enough height to exceed the scroll region
for i in range(15):
    Entry(secondCanvas).pack()

# Create a rectangle in the second canvas
secondCanvas.create_rectangle(50, 100, 150, 600, fill="blue")

# Ensure the second canvas has a scrollable area
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

mainloop()
