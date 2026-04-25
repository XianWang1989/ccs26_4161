
from tkinter import *

def create_scrollable_canvas(root):
    # Create a frame to hold both canvases and scrollbar
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=True)

    # Create the scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Create the first canvas
    first_canvas = Canvas(frame, width=200, height=100)
    first_canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create the second canvas with a large scroll region
    second_canvas = Canvas(frame, width=200, height=100)
    second_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    second_canvas.create_rectangle(0, 0, 200, 5000, fill='lightblue')  # Example content
    second_canvas.config(scrollregion=second_canvas.bbox("all"))

    # Connect the scrollbar to the second canvas
    scrollbar.config(command=second_canvas.yview)
    second_canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to the first canvas
    widget = Label(first_canvas, text='Spam')
    widget.pack()

    # Add more widgets to exceed the height of the canvas
    for i in range(20):
        label = Label(first_canvas, text=f'This is a test label {i+1}')
        label.pack()

    entry = Entry(first_canvas)
    entry.pack()

# Create the main window
root = Tk()
create_scrollable_canvas(root)
root.mainloop()
