
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
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Assume the update file is already downloaded to fname
        # Final command to run the updater
        os.startfile(fname)  # Launch update_myprog.exe

        # Give it a moment before closing
        time.sleep(1)
        self.Destroy()
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
