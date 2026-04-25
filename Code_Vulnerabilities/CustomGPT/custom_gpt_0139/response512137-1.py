
from tkinter import *

root = Tk()

# Create frame to hold both canvases and scrollbar
frame = Frame(root)
frame.pack(expand=True, fill='both')

# Create a scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
firstCanvas = Canvas(frame, width=200, height=400, scrollregion=(0, 0, 0, 1000))
firstCanvas.pack(side="left", fill="both", expand=True)

# Create second canvas
secondCanvas = Canvas(frame, width=200, height=400, scrollregion=(0, 0, 0, 1000))
secondCanvas.pack(side="left", fill="both", expand=True)

# Link scrollbars to both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Create widgets in the first canvas
Label(firstCanvas, text='Spam').pack()
for i in range(20):  # Create multiple labels to enable scrolling
    Label(firstCanvas, text=f"Label {i+1}").pack()

# Create widgets in the second canvas
for i in range(20):  # Create multiple labels to enable scrolling
    Label(secondCanvas, text=f"Label {i+21}").pack()

# Configure each canvas to use the scrollbar
firstCanvas.config(yscrollcommand=scrollbar.set)
secondCanvas.config(yscrollcommand=scrollbar.set)

# Set scrollbar function to update both canvases
scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

# Start Tkinter main loop
mainloop()
