
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
        canupdate = True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Ensure the correct path to the updater executable
            updater_path = os.path.abspath(fname)

            # Download update_myprog.exe to updater_path (not shown here)

            # Close the current app first
            self.Destroy()
            wx.CallAfter(self.run_updater, updater_path)

    def run_updater(self, updater_path):
        # Run the updater independently
        os.startfile(updater_path)  # or use subprocess if you prefer
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
