
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Second canvas
secondCanvas = Canvas(root, width=200, height=300)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure the scrollbar to scroll both canvases
scrollbar.config(command=lambda *args: [firstCanvas.yview(*args), secondCanvas.yview(*args)])

# Set the scroll region for both canvases
firstCanvas.configure(scrollregion=firstCanvas.bbox("all"))
secondCanvas.configure(scrollregion=(0, 0, 200, 5000))  # Set the scroll region for the second canvas

# Create a lot of widgets in the first canvas
for i in range(20):  # Change 20 to the number of widgets you want
    Label(firstCanvas, text=f'This is label {i}').pack()

# Create a large rectangle in the second canvas to visualize scrolling
secondCanvas.create_rectangle((0, 0, 200, 5000), fill='lightblue')  # Create a large rectangle to exceed canvas height
for i in range(50):  # Change 50 to the number of widgets you want in the second canvas
    Label(secondCanvas, text=f'Spam {i}').pack()

# Link the scrollbar to the second canvas
secondCanvas.config(yscrollcommand=scrollbar.set)

mainloop()
