
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=200, height=300)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Link the scroll region of the second canvas
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

# Add widgets to the first canvas
widget1 = Label(firstCanvas, text='This is a test for the first canvas')
widget1.pack()
widget2 = Entry(firstCanvas)
widget2.pack()
for _ in range(20):  # Adding multiple labels to force scrolling
    Label(firstCanvas, text='Spam').pack()

# Add widgets to the second canvas
for _ in range(40):  # Adding more content to the second canvas
    Label(secondCanvas, text='Spam in second canvas').pack()

# Update the scroll region to encompass all widgets
firstCanvas.config(scrollregion=firstCanvas.bbox("all"))
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
