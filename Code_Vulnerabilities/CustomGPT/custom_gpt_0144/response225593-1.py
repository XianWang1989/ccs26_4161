from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:
        print("Selected file:", filename)
        with open("output.txt", "w") as conf:
            conf.write(f"receptor='{filename}'\n")

# Create GUI window
mGui = Tk()
mGui.geometry("500x200")
mGui.title("File Selector")

# Add browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=200, y=80)

mGui.mainloop()
