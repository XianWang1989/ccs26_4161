
from tkinter import *

root = Tk()
root.title("Scrolling Example")

# Create scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000))
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbar to second canvas
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Add widgets to first canvas
for i in range(20):
    label = Label(firstCanvas, text=f'This is label {i}')
    firstCanvas.create_window(100, i * 30, window=label)

# Add widgets to second canvas
for i in range(100):
    entry = Entry(secondCanvas)
    secondCanvas.create_window(100, i * 30, window=entry)

mainloop()
