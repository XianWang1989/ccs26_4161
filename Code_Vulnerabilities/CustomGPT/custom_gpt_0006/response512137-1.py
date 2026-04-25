
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400)
secondCanvas.pack(side="left", fill="both", expand=True)

# Set scrolling region for secondCanvas
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Link scrollbar to secondCanvas
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding widgets to the firstCanvas
Label(firstCanvas, text='Spam').pack()
Label(firstCanvas, text="this is a test").pack()
Entry(firstCanvas).pack()
Label(firstCanvas, text="More content").pack()
Entry(firstCanvas).pack()

# Adding widgets to the secondCanvas
Label(secondCanvas, text='Spam in second canvas').pack()
Label(secondCanvas, text="Another test").pack()
Entry(secondCanvas).pack()
Label(secondCanvas, text="More content").pack()
Entry(secondCanvas).pack()

# Create a scrolling rectangle in the second canvas
secondCanvas.create_rectangle(0, 0, 200, 5000)

# Update scrollregion after adding widgets
secondCanvas.update_idletasks()
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

mainloop()
