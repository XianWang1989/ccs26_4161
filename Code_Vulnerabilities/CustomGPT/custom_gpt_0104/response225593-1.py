
from tkinter import Tk, Button
from tkinter.filedialog import askopenfilename

def browse_file():
    # Ask the user to select a file
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'a') as conf:  # Open a text file in append mode
            conf.write(f'receptor="{filename}"\n')  # Write the filename to the file
        print(f'Selected file: {filename}')  # Print the selected filename (optional)

# Set up the main GUI window
mGui = Tk()
mGui.title('File Browse Example')

# Create the browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the main loop
mGui.mainloop()
