
from tkinter import *

root = Tk()

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas with a larger scrollable area
secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Populate the first canvas with widgets
widgetOne = Label(firstCanvas, text="This is a test")
widgetOne.pack()

# Populate the second canvas with more widgets
for i in range(20):
    Label(secondCanvas, text=f'Spam {i + 1}').pack()

# Create scrollable area in the second canvas
secondCanvas.create_window((0, 0), window=firstCanvas, anchor='nw')
secondCanvas.create_window((0, 200), window=Label(secondCanvas, text='End of Scroll Area'), anchor='nw')

# Run the main loop
mainloop()
