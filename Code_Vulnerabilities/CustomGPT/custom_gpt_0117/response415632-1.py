
import wx
import os
import subprocess
import tempfile
import sys

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Copy your update executable to a temp directory if needed
        # This is where you would download or copy your update_myprog.exe

        # Close the main application
        self.Destroy()

        # Use os.startfile (on Windows) which may help avoid some permissions issues
        os.startfile(fname)  # Adjust fname to the correct path for your updater
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
