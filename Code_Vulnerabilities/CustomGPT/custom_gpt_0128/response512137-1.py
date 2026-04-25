
from tkinter import *

root = Tk()

# Create a Frame to hold the canvases and scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

# Create the first canvas
firstCanvas = Canvas(frame, width=200, height=400)
firstCanvas.pack(side=LEFT, fill=BOTH, expand=True)

# Create the second canvas
secondCanvas = Canvas(frame, width=200, height=400, scrollregion=(0, 0, 0, 5000))
secondCanvas.pack(side=LEFT, fill=BOTH, expand=True)

# Create a scrollbar that will control the second canvas
scrollbar = Scrollbar(frame, command=secondCanvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the second canvas to use the scrollbar
secondCanvas.configure(yscrollcommand=scrollbar.set)

# Add some widgets to the first canvas
Label(firstCanvas, text='Spam 1').pack()
Label(firstCanvas, text='Spam 2').pack()

# Add some widgets to the second canvas
for i in range(50):
    Label(secondCanvas, text=f'Spam {i+3}').pack()

# Create a vertical scrollable area for the second canvas
secondCanvas.create_window((0, 0), window=secondCanvas, anchor='nw')

# Set the scroll region to encompass all items
secondCanvas.update_idletasks()  # Update to recalculate the scrollregion
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
