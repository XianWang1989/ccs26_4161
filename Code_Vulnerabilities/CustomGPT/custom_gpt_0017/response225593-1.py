
import Tkinter as tk
from Tkinter import filedialog

def browse_file():
    # Ask for a file and get the file path
    file_path = filedialog.askopenfilename()
    if file_path:
        with open('output.txt', 'w') as conf:
            conf.write('receptor="{}"\n'.format(file_path))
        print("File path written to output.txt")

# Create the main window
mGui = tk.Tk()
mGui.title('File Selector')

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
