
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
        canupdate = True
        if canupdate:
            # Create a temporary directory for the update executable
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Assuming the update.exe was downloaded into fname

            # Close the current application first
            self.Destroy()
            time.sleep(1)  # Give the application time to close

            # Now run the updater
            subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'], 
                             creationflags=subprocess.DETACHED_PROCESS)

            # Exit the current program
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
