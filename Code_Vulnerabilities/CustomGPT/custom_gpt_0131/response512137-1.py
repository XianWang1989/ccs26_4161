
from tkinter import *

root = Tk()

# Create and pack the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas and set its scroll region
secondCanvas = Canvas(root, width=200, height=100, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Connect the scrollbar to the second canvas's yview
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Create some widgets in the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Add more widgets to the first canvas
for i in range(10):  # Adding multiple widgets to demonstrate scrolling
    Label(firstCanvas, text=f"Label {i+1}").pack()

# Create some widgets in the second canvas
Label(secondCanvas, text='Spam').pack()
for i in range(20):  # Adding multiple widgets to demonstrate scrolling
    Entry(secondCanvas).pack()

mainloop()
