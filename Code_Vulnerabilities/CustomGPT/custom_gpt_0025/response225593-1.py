
import Tkinter as tk
import tkFileDialog

def browse_file():
    # Open the file dialog and get the selected file path
    file_path = tkFileDialog.askopenfilename()
    if file_path:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(file_path))
        print("File path saved to output.txt:", file_path)

# Create the main application window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the 'Browse' button and set its command
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the Tkinter event loop
mGui.mainloop()
