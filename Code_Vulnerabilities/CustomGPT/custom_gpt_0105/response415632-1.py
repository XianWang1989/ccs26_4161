
import wx
import subprocess
import win32process
import tempfile
import os
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
            # Start the update program without being a child
            proc = subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'], 
                                    creationflags=win32process.DETACHED_PROCESS)
            self.Destroy()
            time.sleep(1)  # Allow time for the frame to close
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
