
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)
firstCanvas.configure(yscrollcommand=scrollbar.set)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=5000, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side="left", fill="both", expand=True)
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Widgets in first canvas
widgetOne = Label(firstCanvas, text="This is a test")
widgetOne.pack()
widgetTwo = Entry(firstCanvas)
widgetTwo.pack()

# Widgets in second canvas
widgetThree = Label(secondCanvas, text='Spam')
widgetThree.pack()
widgetFour = Entry(secondCanvas)
widgetFour.pack()

# Adding space in second canvas
for i in range(0, 50):
    Label(secondCanvas, text=f'Label {i}').pack()

mainloop()
