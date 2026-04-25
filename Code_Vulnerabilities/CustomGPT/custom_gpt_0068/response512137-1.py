
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Set up the first canvas
firstCanvas = Canvas(root, width=200, height=100, scrollregion=(0,0,0,5000))
firstCanvas.pack(side="left", fill="both", expand=True)

# Set up the second canvas
secondCanvas = Canvas(root, width=200, height=5000, scrollregion=(0,0,0,5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure the scrollbar to control the second canvas
scrollbar.config(command=secondCanvas.yview)

# Add a rectangle to the second canvas
secondCanvas.create_rectangle((200, 300, 300, 600), fill="blue")

# Adding widgets to first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Adding more widgets to the first canvas
for i in range(30):  # Example to create multiple widgets
    Label(firstCanvas, text=f"This is test label {i+1}").pack()

# Adding widgets to second canvas
widgetThree = Label(secondCanvas, text='Spam')
widgetThree.pack()   
widgetFour = Entry(secondCanvas)
widgetFour.pack()

# Adding more widgets to the second canvas
for i in range(30):  # Example to create multiple widgets
    Entry(secondCanvas).pack()

mainloop()
