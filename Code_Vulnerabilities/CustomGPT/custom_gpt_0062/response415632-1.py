
import wx
import subprocess
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
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Ensure the update executable is downloaded or available here

        # Close the main application
        self.Destroy()
        time.sleep(1)  # Ensure the window is fully closed

        # Launch the updater without a subprocess
        os.startfile(fname)  # This launches the updater as a separate process
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
