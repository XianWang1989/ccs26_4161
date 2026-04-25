
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
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Start the update process without waiting for it to complete
        subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password=pw'], 
                         creationflags=win32process.DETACHED_PROCESS)

        # Close the current application
        self.Destroy()
        wx.CallAfter(sys.exit)

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
