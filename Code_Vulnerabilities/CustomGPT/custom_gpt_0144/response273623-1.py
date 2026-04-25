def nextq(self):
    self.master.destroy()  # Close the current window
    root = Tk()            # Create a new root window for the next question
    q2(root)
