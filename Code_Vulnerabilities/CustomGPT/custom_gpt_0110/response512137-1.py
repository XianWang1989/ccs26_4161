
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Frame to hold the canvases
frame = Frame(root)
frame.pack(side=LEFT, fill=BOTH, expand=True)

# First Canvas
firstCanvas = Canvas(frame, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)
firstCanvas.create_window((0, 0), window=Label(firstCanvas, text='Spam'), anchor='nw')

# Second Canvas
secondCanvas = Canvas(frame, width=200, height=400, scrollregion=(0, 0, 200, 400))
secondCanvas.pack(side="left", fill="both", expand=True)

# Add multiple widgets to the second canvas
for i in range(20):
    Label(secondCanvas, text=f'This is label {i}').pack()

# Linking scrollbar
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Allowing scrolling
firstCanvas.bind('<Configure>', lambda e: firstCanvas.configure(scrollregion=firstCanvas.bbox('all')))
secondCanvas.bind('<Configure>', lambda e: secondCanvas.configure(scrollregion=secondCanvas.bbox('all')))

mainloop()
