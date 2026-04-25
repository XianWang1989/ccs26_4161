
import wx
import subprocess
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
        canupdate = True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Assuming the update_myprog.exe is downloaded to fname

            # Close the main app
            self.Destroy()
            wx.CallAfter(self.launch_updater, fname)  # Launch the updater after destroying the app

    def launch_updater(self, updater_path):
        # Launch the updater as a separate process
        subprocess.Popen(updater_path, creationflags=subprocess.CREATE_NO_WINDOW)
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
