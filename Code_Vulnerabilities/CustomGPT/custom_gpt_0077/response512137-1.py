
from tkinter import *

root = Tk()

# Create a frame to hold the canvases and scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

# Create vertical scrollbar
scrollbar = Scrollbar(frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(frame, width=200, height=300)
firstCanvas.pack(side="left", fill=BOTH, expand=True)

# Create second canvas
secondCanvas = Canvas(frame, width=200, height=300, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill=BOTH, expand=True)

# Create a rectangle on the second canvas
secondCanvas.create_rectangle(50, 50, 150, 100, fill="blue")

# Add widgets to the first canvas
for i in range(30):
    widget = Label(firstCanvas, text=f'This is label {i+1}')
    widget.pack()

# Add widgets to the second canvas
for i in range(30):
    widget = Label(secondCanvas, text=f'Spam {i+1}')
    widget.pack()

# Link scrollbar to both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

mainloop()
