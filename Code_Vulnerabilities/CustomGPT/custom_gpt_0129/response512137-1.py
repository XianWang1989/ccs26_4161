
from tkinter import *

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
firstCanvas = Canvas(root, width=200, height=100)
firstCanvas.pack(side="left", fill="both", expand=True)
firstCanvas.config(yscrollcommand=scrollbar.set)

# Second Canvas
secondCanvas = Canvas(root, width=200, height=10000)
secondCanvas.pack(side="left", fill="both", expand=True)
secondCanvas.create_rectangle((0, 0, 200, 5000))  # Just for visual reference
secondCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Widgets in the first canvas
widget = Label(firstCanvas, text='Spam')
widget.pack()

# Other Widgets in the first canvas
for i in range(20):  # Adding multiple widgets to fill the first canvas
    widget = Label(firstCanvas, text=f'This is a test {i + 1}')
    widget.pack()

# Widgets in the second canvas
widgetThree = Label(secondCanvas, text='Spam')
widgetThree.pack()
widgetFour = Entry(secondCanvas)
widgetFour.pack()

# Configure scrollbar
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Update the scrollregion after adding all widgets
firstCanvas.update_idletasks()
secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Run the main loop
mainloop()
