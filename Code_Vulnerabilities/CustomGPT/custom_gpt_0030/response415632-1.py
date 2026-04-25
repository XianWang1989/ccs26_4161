
import os
import wx
import tempfile
import sys
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
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Ensure you download update_myprog.exe to fname here

            # Close the application before running the updater
            self.Destroy()
            time.sleep(0.1)  # Give the GUI a moment to close

            # Use os.startfile to run the updater independently
            os.startfile(fname)
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
