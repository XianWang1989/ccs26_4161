
import wx
import os
import sys
import tempfile
import time

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        canupdate = True
        if canupdate:
            # Create a temporary directory for the update executable
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')

            # Wait a moment for cleanup processes to finish
            self.Destroy()  # Close the main app window
            time.sleep(1)  # Allow time for closure

            # Use os.startfile to run the updater
            os.startfile(fname)  # Start update_myprog.exe

            # Exit the current app
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
