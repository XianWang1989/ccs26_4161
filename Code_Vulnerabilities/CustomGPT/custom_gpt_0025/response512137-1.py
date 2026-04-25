
from tkinter import *

# Create the main window
root = Tk()

# Create a vertical scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create two canvases
firstCanvas = Canvas(root, width=200, height=400)
firstCanvas.pack(side="left", fill="both", expand=True)

secondCanvas = Canvas(root, width=200, height=400, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a frame to hold the content of the first canvas
frame1 = Frame(firstCanvas)
firstCanvas.create_window((0, 0), window=frame1, anchor='nw')

# Create a frame to hold the content of the second canvas
frame2 = Frame(secondCanvas)
secondCanvas.create_window((0, 0), window=frame2, anchor='nw')

# Add widgets to the first canvas
for i in range(20):
    Label(frame1, text=f'This is label {i}').pack()

# Add widgets to the second canvas
for i in range(50):
    Label(frame2, text=f'This is label {i} in second canvas').pack()

# Configure scrollbar
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Ensure the canvas updates its scrolling region
def update_scrollregion(event):
    firstCanvas.configure(scrollregion=firstCanvas.bbox("all"))
    secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

firstCanvas.bind("<Configure>", update_scrollregion)
secondCanvas.bind("<Configure>", update_scrollregion)

# Start the main loop
mainloop()
