
import wx
import subprocess
import os
import sys
import tempfile

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
            # Ensure the path to update_myprog.exe is correct
            # Using the correct method to start the updater detached
            updater_path = r"path\to\your\update_myprog.exe"  # Update this line
            subprocess.Popen(updater_path, creationflags=subprocess.CREATE_NEW_CONSOLE)  # Using CREATE_NEW_CONSOLE to detach
            self.Destroy()
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
