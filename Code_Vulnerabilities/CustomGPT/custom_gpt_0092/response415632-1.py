
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
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # First, use os.startfile instead of Popen to run the updater
        subprocess.Popen([os.path.join(os.getcwd(), 'update_myprog.exe'), '/SP-', '/silent', '/noicons', '/nocancel', '/password=pw'], 
                         creationflags=subprocess.DETACHED_PROCESS)

        # Close the main program after starting the updater
        self.Destroy()
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
