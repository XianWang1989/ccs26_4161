
import wx
import subprocess
import win32process
import sys
import os
import tempfile
import time

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        canupdate = True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')

            # Use subprocess to run the update executable
            # Make sure to use the full path to update_myprog.exe

            # Freezing the wx application
            self.Destroy()
            time.sleep(1)  # Give time to clean up UI and finish events

            # Run the update executable
            subprocess.Popen([fname], creationflags=win32process.DETACHED_PROCESS)

            # Exit the main program
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
