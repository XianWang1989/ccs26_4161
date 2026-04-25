
from tkinter import *

root = Tk()

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=400)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure the scrollbar to scroll both canvases
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Adding a lot of widgets to ensure scrolling is necessary
for i in range(20):
    Label(firstCanvas, text=f'Label {i}').pack()

# Scroll region for the second canvas
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Adding a lot of widgets to the second canvas as well
for i in range(50):
    Label(secondCanvas, text=f'Spam {i}').pack()

mainloop()
