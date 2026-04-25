
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
            # Specify the correct path for the update executable
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Use Popen without DETACHED_PROCESS
            subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'])
            self.Destroy()
            # Ensure the main program exits completely
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
