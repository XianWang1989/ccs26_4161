
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 0, 1000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)
secondCanvas.create_rectangle(0, 0, 200, 1000, fill='lightblue')

# Sample widgets in first canvas
widget1 = Label(firstCanvas, text='Widget 1')
widget1.pack()

widget2 = Label(firstCanvas, text='Widget 2')
widget2.pack()

# Sample widgets in second canvas that extend beyond the screen
for i in range(50):
    Label(secondCanvas, text=f'Spam {i}').pack()

# Scrollbar configuration
scrollbar.config(command=secondCanvas.yview)

mainloop()
