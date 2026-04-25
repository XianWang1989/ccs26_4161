
from tkinter import *

# Create main window
root = Tk()

# Create a vertical scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Set up first canvas
firstCanvas = Canvas(root, width=200, height=500)
firstCanvas.pack(side="left", fill="both", expand=True)

# Set up second canvas
secondCanvas = Canvas(root, width=200, height=500)
secondCanvas.pack(side="left", fill="both", expand=True)

# Create a combined scroll region for both canvases
combined_scrollregion = (0, 0, 0, 1000)  # Adjust the height as needed

# Configure the scrollbar to control both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Link scrollbar with both canvases
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Add a lot of widgets to first canvas
for i in range(20):
    widget = Label(firstCanvas, text=f'This is a test {i + 1}')
    widget.pack()

# Add a rectangle to the second canvas
secondCanvas.create_rectangle((200, 300, 300, 600), outline="black", fill="blue")

# Add some widgets to the second canvas
for j in range(20):
    widget = Label(secondCanvas, text=f'Label {j + 1} on second canvas')
    widget.pack()

# Set scrollregion for both canvases
firstCanvas.configure(scrollregion=firstCanvas.bbox("all"))
secondCanvas.configure(scrollregion=combined_scrollregion)

# Start the main loop
mainloop()
