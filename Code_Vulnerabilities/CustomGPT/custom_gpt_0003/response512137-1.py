
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=400)  # Adjust height for visibility
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0,0,0,5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link the scrollbar to the second canvas
scrollbar.config(command=lambda *args: (secondCanvas.yview(*args), firstCanvas.yview(*args)))

# Create some widgets in the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Add additional widgets for testing scroll
for i in range(20):
    label = Label(firstCanvas, text=f"This is a test label {i+1}")
    label.pack()

# Create some widgets in the second canvas
widgetThree = Label(secondCanvas, text='Spam in second canvas')
widgetThree.pack()

# Add widgets to second canvas
for i in range(50):
    entry = Entry(secondCanvas)
    entry.pack()

# Keep the main loop running
mainloop()
