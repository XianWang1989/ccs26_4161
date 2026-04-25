
import wx
import subprocess
import os
import tempfile
import sys

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Copy or download the update_myprog.exe to fname
        # Assuming the update_exe is already stored at the expected location for simplicity.

        # Schedule the update and exit
        subprocess.Popen([fname, "/SP-", "/silent", "/noicons", "/nocancel", "/password=pw"],
                         creationflags=subprocess.DETACHED_PROCESS)
        self.Destroy()  # Close the current window
        wx.CallAfter(sys.exit)  # Ensure the program exits after closure

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
