
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas with a vertical scrollbar
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas and set up its scroll region
secondCanvas = Canvas(root, width=200, height=500, scrollregion=(0, 0, 200, 1000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link the scrollbar to both canvases
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Adding some widgets to the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Adding multiple widgets in firstCanvas so it exceeds the height
for i in range(30):
    Label(firstCanvas, text=f'This is a test {i + 1}').pack()

# Adding widgets to the second canvas
for i in range(30, 60):
    Label(secondCanvas, text=f'Additional content {i + 1}').pack()

# Main loop
mainloop()
