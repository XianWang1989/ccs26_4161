
import wx
import os
import tempfile
import sys

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        # Change this variable to check if the update can proceed
        canupdate = True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')

            # Replace this line with os.startfile()
            os.startfile(fname)  # Start the updater

            self.Destroy()  # Close the current application
            sys.exit()  # Exit the application

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
