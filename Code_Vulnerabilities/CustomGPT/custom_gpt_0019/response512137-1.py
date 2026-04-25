
from tkinter import *

root = Tk()

# Create a frame to hold the canvases and scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

# Create the scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(frame, width=200, height=400)
firstCanvas.pack(side="left", fill=BOTH, expand=True)

# Create the second canvas
secondCanvas = Canvas(frame, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill=BOTH, expand=True)

# Link scrollbar to the second canvas
scrollbar.config(command=secondCanvas.yview)

# Populate the first canvas with widgets
widget1 = Label(firstCanvas, text='Label 1')
widget1.pack()

widget2 = Label(firstCanvas, text='Label 2')
widget2.pack()

# Populate the second canvas with widgets
for i in range(50):
    Label(secondCanvas, text=f'Spam {i}').pack()

# Update the scroll region of the second canvas
secondCanvas.update_idletasks()  # Necessary to update scroll region
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

mainloop()
