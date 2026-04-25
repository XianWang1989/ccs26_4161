
from tkinter import *

root = Tk()

# Create a main frame to hold the canvases and scrollbar
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

# Create a canvas to hold both canvases
combinedCanvas = Canvas(main_frame, width=400, height=400)
combinedCanvas.pack(side=LEFT, fill=BOTH, expand=True)

# Create a vertical scrollbar
scrollbar = Scrollbar(main_frame, command=combinedCanvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the combined canvas to work with the scrollbar
combinedCanvas.configure(yscrollcommand=scrollbar.set)

# Create a frame within the combined canvas to hold the two canvases
frame = Frame(combinedCanvas)
combinedCanvas.create_window((0, 0), window=frame, anchor='nw')

# Create first canvas and fill it with widgets
firstCanvas = Frame(frame, width=200, height=400)
firstCanvas.pack(side=TOP, fill=BOTH, expand=True)

# Add widgets to the first canvas
Label(firstCanvas, text='Spam').pack()
Label(firstCanvas, text="this is a test").pack()
Entry(firstCanvas).pack()
Label(firstCanvas, text='Another label').pack()

# Create second canvas and fill it with widgets
secondCanvas = Frame(frame, width=200, height=400)
secondCanvas.pack(side=TOP, fill=BOTH, expand=True)

# Add widgets to the second canvas
Label(secondCanvas, text='Spam 2').pack()
Entry(secondCanvas).pack()
Label(secondCanvas, text='Another entry').pack()

# Update the scroll region of the combined canvas
frame.update_idletasks()  # Update "requested size" for the frame
combinedCanvas.config(scrollregion=combinedCanvas.bbox("all"))

# Run the Tkinter main loop
mainloop()
