
from tkinter import *

def setup_scrollable_frame(root):
    # Create a frame that will hold both canvases
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=True)

    # Create the scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Create the first canvas
    firstCanvas = Canvas(frame, width=200, height=300)
    firstCanvas.pack(side="left", fill=BOTH, expand=True)

    # Create the second canvas
    secondCanvas = Canvas(frame, width=200, height=300, scrollregion=(0, 0, 0, 5000))
    secondCanvas.pack(side="left", fill=BOTH, expand=True)

    # Configure scrollbars to the canvases
    scrollbar.config(command=lambda *args: (firstCanvas.yview(*args), secondCanvas.yview(*args)))

    # Create content for the first canvas
    for i in range(20):
        label = Label(firstCanvas, text=f'This is label {i}')
        label.pack()

    # Create content for the second canvas
    for i in range(50):
        label = Label(secondCanvas, text=f'This is label {i}')
        label.pack()

    # Link the scrollbar to the second canvas for vertical scrolling
    secondCanvas.config(yscrollcommand=scrollbar.set)

    # Adjusting scroll region for the second canvas
    secondCanvas.configure(scrollregion=secondCanvas.bbox("all"))

# Create the root window and set up the scrollable frame
root = Tk()
setup_scrollable_frame(root)
mainloop()
