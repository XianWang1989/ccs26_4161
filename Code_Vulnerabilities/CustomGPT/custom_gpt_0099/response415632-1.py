
import wx
import subprocess
import tempfile
import os
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

        # Assume the update exe is downloaded to fname
        # Replace the line below with actual download logic
        # e.g., download_file("http://example.com/update_myprog.exe", fname)

        # Launch the updater using os.startfile to avoid process inheritance
        os.startfile(fname)  # This will run the updater independently

        self.Destroy()  # Close the current application window
        sys.exit()      # Exit the application

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
