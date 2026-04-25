
from tkinter import *

def on_canvas configure(event):
    firstCanvas.configure(scrollregion=firstCanvas.bbox("all"))
    secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

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

# Create widgets in the first canvas
Label(firstCanvas, text='Spam').pack()
for i in range(15):
    Label(firstCanvas, text=f'This is a test {i}').pack()

firstCanvas.bind('<Configure>', on_canvas_configure)

# Create widgets in the second canvas
Label(secondCanvas, text='Spam').pack()
for i in range(50):
    Entry(secondCanvas).pack()

# Scrollbar configuration
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Set scroll region
firstCanvas.configure(scrollregion=firstCanvas.bbox("all"))
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Run the application
mainloop()
