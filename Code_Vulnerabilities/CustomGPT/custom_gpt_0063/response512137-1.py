
from tkinter import *

def on_canvas_configure(event):
    # Update scrollregion after adding new widgets
    firstCanvas.configure(scrollregion=firstCanvas.bbox("all"))
    secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

root = Tk()

# Create scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas with scroll region
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Sample widgets for the first canvas
Label(firstCanvas, text='Spam').pack()
Label(firstCanvas, text="This is a test").pack()
Entry(firstCanvas).pack()
Label(firstCanvas, text='More content...').pack()

# Sample widgets for the second canvas
Label(secondCanvas, text='Spam').pack()
Entry(secondCanvas).pack()
Label(secondCanvas, text='More content...').pack()

# Configure scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Bind the configure event to update the scrollregion
firstCanvas.bind("<Configure>", on_canvas_configure)
secondCanvas.bind("<Configure>", on_canvas_configure)

mainloop()
