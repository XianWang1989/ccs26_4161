
from tkinter import *

root = Tk()

# Create scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create frame to hold widgets on the first canvas
frame1 = Frame(firstCanvas)
firstCanvas.create_window((0, 0), window=frame1, anchor='nw')

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create frame to hold widgets on the second canvas
frame2 = Frame(secondCanvas)
secondCanvas.create_window((0, 0), window=frame2, anchor='nw')

# Populate the first canvas with widgets
widget = Label(frame1, text='Spam')
widget.pack()

# Lots of widgets in the first canvas
for i in range(15):
    widgetOne = Label(frame1, text=f"This is test {i + 1}")
    widgetOne.pack()

# Populate the second canvas with widgets
widgetThree = Label(frame2, text='Spam')
widgetThree.pack()

widgetFour = Entry(frame2)
widgetFour.pack()

# Configure scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Main loop
mainloop()
