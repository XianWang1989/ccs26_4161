
from tkinter import *

def update_scrollregion(event):
    first_canvas.update_idletasks()
    second_canvas.config(scrollregion=second_canvas.bbox("all"))

root = Tk()

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# First Canvas
first_canvas = Canvas(root, width=200, height=300)
first_canvas.pack(side="left", fill="both", expand=True)

# Second Canvas
second_canvas = Canvas(root, width=200, height=300, scrollregion=(0, 0, 0, 5000), yscrollcommand=scrollbar.set)
second_canvas.pack(side="left", fill="both", expand=True)

# Connect scrollbar to second canvas
scrollbar.config(command=second_canvas.yview)

# Add content to first canvas
Label(first_canvas, text='Spam').pack()
Label(first_canvas, text="This is a test").pack()
Entry(first_canvas).pack()
Label(first_canvas, text='Another label').pack()

# Add some sample content to the second canvas
for i in range(30):
    Label(second_canvas, text=f'Spam {i}').pack()

# Update scrollregion to fit the content
second_canvas.bind("<Configure>", update_scrollregion)

mainloop()
