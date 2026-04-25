
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
        # Simulating update download and path setup
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')
        # Ideally, you would download update_myprog.exe into `fname` here.

        # Using os.startfile instead of subprocess.Popen
        os.startfile(fname)  # This will launch the updater executable.

        wx.CallAfter(self.Destroy)  # Safely close the wx.Frame
        wx.CallAfter(sys.exit)  # Exit the application

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
