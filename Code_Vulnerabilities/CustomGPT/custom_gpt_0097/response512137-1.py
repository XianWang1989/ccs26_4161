
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 1000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbar to both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Adding widgets to the first canvas
widget_one = Label(firstCanvas, text="This is a test")
widget_one.pack()
widget_two = Entry(firstCanvas)
widget_two.pack()
for i in range(20):
    Label(firstCanvas, text=f"Label {i+1}").pack()

# Adding widgets to the second canvas
secondCanvas.create_rectangle((200, 300, 300, 600))
for i in range(40):
    Label(secondCanvas, text=f"Spam {i + 1}").pack()

mainloop()
