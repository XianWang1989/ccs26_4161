
import os
import sys
import wx
import subprocess
import win32process
import tempfile
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

            # Start the Update process
            proc = subprocess.Popen(
                [fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'],
                creationflags=win32process.CREATE_NO_WINDOW
            )
            # Sleep for a short time to ensure the subprocess starts
            time.sleep(1)
            self.Destroy()
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
