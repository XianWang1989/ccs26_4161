
from tkinter import *

root = Tk()

# Create scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(root, width=200, height=300)
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbar to second canvas
scrollbar.config(command=secondCanvas.yview)

# Add content to first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Add multiple widgets to first canvas
for i in range(20):
    Label(firstCanvas, text=f'This is a test {i + 1}').pack()

# Add multiple widgets to second canvas
for i in range(50):
    Label(secondCanvas, text=f'Spam {i + 1}').pack()

# Update scrollregion to include all widgets
secondCanvas.update_idletasks()
secondCanvas.config(scrollregion=secondCanvas.bbox("all"))

mainloop()
