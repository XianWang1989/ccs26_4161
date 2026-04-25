
from tkinter import *

root = Tk()

# Create the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Set up the first canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Set up the second canvas
secondCanvas = Canvas(root, width=200, height=300)
secondCanvas.pack(side="left", fill="both", expand=True)

# Configure the scrollbar to scroll the second canvas
scrollbar.config(command=secondCanvas.yview)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Create a scroll region for the second canvas
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Add widgets to the first canvas
Label(firstCanvas, text='Spam').pack()
Label(firstCanvas, text="this is a test").pack()
Entry(firstCanvas).pack()

# Add a lot of widgets to the second canvas
for i in range(50):
    Label(secondCanvas, text=f"Label {i}").pack()

# Create a rectangle for visual reference
secondCanvas.create_rectangle((20, 20, 180, 200), fill="lightblue")

# Update scroll region to include all content in the second canvas
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

mainloop()
