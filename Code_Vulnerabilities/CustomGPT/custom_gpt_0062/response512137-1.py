
from tkinter import *

root = Tk()

# Define the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the two canvases
firstCanvas = Canvas(root, width=200, height=400, bg='lightblue')
firstCanvas.pack(side="left", fill="both", expand=True)

secondCanvas = Canvas(root, width=200, height=400, bg='lightgreen')
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure the scrollbar to scroll the second canvas
secondCanvas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=secondCanvas.yview)

# Create a frame in the second canvas to hold its content
secondFrame = Frame(secondCanvas)
secondCanvas.create_window((0, 0), window=secondFrame, anchor='nw')

# Populate the first canvas
widgetOne = Label(firstCanvas, text="This is a test")
widgetOne.pack()
widgetTwo = Entry(firstCanvas)
widgetTwo.pack()
widgetThree = Label(firstCanvas, text='Spam')
widgetThree.pack()

# Populate the second canvas with multiple widgets
for i in range(20):
    label = Label(secondFrame, text=f'Item {i+1}')
    label.pack()

# Update the scrollregion of the second canvas
secondFrame.update_idletasks()
secondCanvas.config(scrollregion=secondCanvas.bbox('all'))

mainloop()
