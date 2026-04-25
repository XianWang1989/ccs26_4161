
from tkinter import *

root = Tk()

# Scrollbar setup
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=5000, scrollregion=(0, 0, 200, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Adding content to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

for i in range(30):  # Adding more widgets for testing
    widgetOne = Label(firstCanvas, text=f"This is test label {i+1}")
    widgetOne.pack()

# Adding content to the second canvas
for i in range(100):  # Lots of widgets to make it scrollable
    widgetTwo = Label(secondCanvas, text=f"Label {i+1} on second canvas")
    widgetTwo.pack()

# Configure the scrollbar to scroll both canvases
def scroll(event):
    firstCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
    secondCanvas.yview_scroll(int(-1*(event.delta/120)), "units")

scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))
root.bind_all("<MouseWheel>", scroll)

mainloop()
