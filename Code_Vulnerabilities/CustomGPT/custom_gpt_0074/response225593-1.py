
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    # Open a file dialog and store the selected file's path
    file_path = askopenfilename()
    if file_path:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open a text file to write
            conf.write('receptor="' + file_path + '"\n')  # Write to the file
        print("File path written to output.txt:", file_path)  # Optional print statement

# Create a simple GUI
mGui = Tk()
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
