
import wx
import subprocess
import os
import sys
import tempfile
import win32process

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
            # Make sure to copy update_myprog.exe into the temp directory or set the path accordingly
            # subprocess.call can be used here to run the installer
            update_command = f'"{fname}" /SP- /silent /noicons /nocancel /password="pw"'

            # Close the application before running the update
            self.Destroy()
            # Run the updater in a new command prompt process
            subprocess.Popen(update_command, creationflags=win32process.DETACHED_PROCESS, shell=True)
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
