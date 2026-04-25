
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

        # Prepare the update command
        command = f'"{fname}" /SP- /silent /noicons /nocancel /password="pw"'

        # Start updater as a separate process
        subprocess.Popen(command, creationflags=subprocess.DETACHED_PROCESS, shell=True)

        # Delay to ensure the subprocess starts
        time.sleep(1)

        # Close the application
        self.Destroy()
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
