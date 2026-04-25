
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=200, height=300)
secondCanvas.pack(side="left", fill="both", expand=True)

# Set the scrollregion for the second canvas
secondCanvas.configure(scrollregion=(0, 0, 0, 5000))

# Link scrollbar and second canvas
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Add widgets to the first canvas
Label(firstCanvas, text='Spam').pack()
Label(firstCanvas, text="This is a test").pack()
Entry(firstCanvas).pack()
Label(firstCanvas, text='More Spam').pack()

# Add widgets to the second canvas
for i in range(10):  # Adding multiple labels to exceed the canvas height
    Label(secondCanvas, text=f'Spam {i}').pack()

mainloop()
