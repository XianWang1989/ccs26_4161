
from Tkinter import Tk, Button, askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog and get the filename
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open the output file
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the file
        print("File saved:", filename)  # Optional: print to console for confirmation

mGui = Tk()
browsebutton = Button(mGui, text='Browse', command=browse_file)  # Call browse_file instead
browsebutton.place(x=400, y=50)

mGui.mainloop()
