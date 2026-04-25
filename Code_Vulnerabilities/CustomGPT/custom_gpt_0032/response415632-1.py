
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
        can_update = True
        if can_update:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Start the updater
            updater_path = os.path.join(tempdir, "update_myprog.exe")

            # Start update_myprog.exe without waiting for it to finish
            subprocess.Popen(updater_path, creationflags=subprocess.DETACHED_PROCESS)

            # Optional: Delay for a moment to ensure the updater gets the control
            time.sleep(1)

            # Destroy the current app
            self.Destroy()
            # Proper exit
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
