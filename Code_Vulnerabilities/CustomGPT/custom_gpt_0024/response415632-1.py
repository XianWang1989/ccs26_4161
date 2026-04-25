
import wx
import subprocess
import os
import sys
import tempfile
import ctypes

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        # Close the application first
        self.Destroy()
        # Create a temporary directory to store the updater
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Start the update executable without waiting for it to finish
        subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password=pw'], 
                         creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

        # Exit the original program
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
