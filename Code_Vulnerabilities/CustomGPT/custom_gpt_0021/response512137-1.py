
from tkinter import *

root = Tk()

# Create a main frame to hold the canvases and scrollbar
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

# Create the scrollbar
scrollbar = Scrollbar(main_frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the first canvas
first_canvas = Canvas(main_frame, width=200, height=500)
first_canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Create the second canvas with a scroll region
second_canvas = Canvas(main_frame, width=200, height=500, scrollregion=(0, 0, 0, 1000), yscrollcommand=scrollbar.set)
second_canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Configure the scrollbar
scrollbar.config(command=second_canvas.yview)

# Add content to the first canvas
Label(first_canvas, text='Spam').pack()
Label(first_canvas, text="this is a test").pack()
Entry(first_canvas).pack()
Label(first_canvas, text='More Labels...').pack()

# Adding content to the second canvas
for i in range(50):
    Label(second_canvas, text=f'Label {i}').pack()

# Make sure to connect the scrollbar to the second canvas
second_canvas.create_window((0, 0), window=first_canvas, anchor='nw')

# Set the scroll region for the second canvas
second_canvas.update_idletasks()  # Update to ensure the scroll region is correct
second_canvas.config(scrollregion=second_canvas.bbox("all"))

mainloop()
