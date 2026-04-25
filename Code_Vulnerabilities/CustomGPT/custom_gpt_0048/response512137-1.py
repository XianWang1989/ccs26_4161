
from tkinter import *

root = Tk()
root.geometry("400x400")  # Set a window size

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=400)
secondCanvas.pack(side="left", fill="both", expand=True)

# Set the scroll region for the second canvas
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Create widgets for the first canvas
for i in range(20):
    label = Label(firstCanvas, text=f'Label {i}')
    label.pack()

# Create lots of widgets for the second canvas
for i in range(50):
    label = Label(secondCanvas, text=f'Spam {i}')
    label.pack()

# Link the scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Allow the scrollbar to scroll both canvases
def onScroll(*args):
    firstCanvas.yview(*args)
    secondCanvas.yview(*args)

scrollbar.config(command=onScroll)

mainloop()
