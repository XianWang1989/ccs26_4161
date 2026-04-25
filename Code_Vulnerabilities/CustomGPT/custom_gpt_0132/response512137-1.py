
from tkinter import *

root = Tk()
root.geometry("600x400")

# Create a vertical scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas and its frame
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas and configure scroll region
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure the scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Adding widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()
widgetOne = Label(firstCanvas, text="this is a test")
widgetOne.pack()
widgetTwo = Entry(firstCanvas)
widgetTwo.pack()

# Adding widgets to the second canvas
for i in range(15):  # Create multiple entries to force scrolling
    widgetThree = Label(secondCanvas, text=f'This is item {i + 1}')
    widgetThree.pack()

# Run the application
mainloop()
