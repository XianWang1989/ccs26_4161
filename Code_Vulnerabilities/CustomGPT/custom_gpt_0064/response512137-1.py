
from tkinter import *

# Create the main window
root = Tk()
root.geometry("400x400")

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
firstCanvas = Canvas(root, width=200, height=300, bg='lightblue')
firstCanvas.pack(side="left", fill="both", expand=True)

# Create the second canvas
secondCanvas = Canvas(root, width=200, height=300, bg='lightgreen')
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Add content to the first canvas
for i in range(20):
    widget = Label(firstCanvas, text=f'Label {i+1}')
    firstCanvas.create_window(100, i*30, window=widget)

# Add content to the second canvas
for i in range(20):
    widget = Label(secondCanvas, text=f'Label {i+1}')
    secondCanvas.create_window(100, i*30, window=widget)

# Update the scroll region of both canvases
firstCanvas.config(scrollregion=firstCanvas.bbox("all"))
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

# Start the main loop
mainloop()
