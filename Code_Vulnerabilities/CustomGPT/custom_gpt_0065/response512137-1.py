
from tkinter import *

# Create main window
root = Tk()

# Create scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(root, width=200, height=400)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure scrollbar
scrollbar.config(command=secondCanvas.yview)

# Add scroll region to second canvas
secondCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.configure(scrollregion=(0, 0, 0, 5000))

# Add widgets to first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Add multiple widgets to first canvas
for i in range(30):
    Label(firstCanvas, text=f"This is a test {i+1}").pack()

# Add widgets to second canvas
widgetThree = Label(secondCanvas, text='Spam in second canvas')
widgetThree.pack()
for i in range(30):
    Entry(secondCanvas).pack()

# Create a rectangle to illustrate scrolling
secondCanvas.create_rectangle((50, 300, 150, 600), fill="blue")

# Run the application
mainloop()
