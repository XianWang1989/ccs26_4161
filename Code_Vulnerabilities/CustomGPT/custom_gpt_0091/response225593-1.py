
from tkinter import Tk, Button, filedialog

# Function to open the file dialog and get the file path
def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected file:", file_path)
        # Write the selected file path to a text file
        with open('output.txt', 'w') as conf:
            conf.write(f'receptor="{file_path}"\n')

# Create the main window
mGui = Tk()
mGui.title("File Selector")

# Create a Browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the Tkinter event loop
mGui.mainloop()
