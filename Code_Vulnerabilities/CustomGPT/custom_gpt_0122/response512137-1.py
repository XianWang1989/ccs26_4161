
from tkinter import *

root = Tk()

# Create a frame to hold both canvases
frame = Frame(root)
frame.pack(side="left", fill="both", expand=True)

# Create a scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create first canvas
first_canvas = Canvas(frame, width=200, height=300, yscrollcommand=scrollbar.set)
first_canvas.pack(side="top", fill="both", expand=True)

# Create second canvas
second_canvas = Canvas(frame, width=200, height=300, yscrollcommand=scrollbar.set)
second_canvas.pack(side="top", fill="both", expand=True)

# Link scrollbar to both canvases
scrollbar.config(command=lambda *args: (first_canvas.yview(*args), second_canvas.yview(*args)))

# Add widgets to first canvas
widget = Label(first_canvas, text='Spam')
widget.pack()

# Add multiple widgets to first canvas for scrolling
for i in range(20):
    widget = Label(first_canvas, text=f"This is a test {i + 1}")
    widget.pack()

# Add widgets to second canvas
for i in range(10):
    widget = Label(second_canvas, text=f"Spam {i + 1}")
    widget.pack()

# Set the scrollregion for the second canvas
second_canvas.configure(scrollregion=second_canvas.bbox("all"))

# Run the application
mainloop()
