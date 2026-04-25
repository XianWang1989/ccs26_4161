
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

        # Assuming update_myprog.exe is already in the correct path
        # Move or download update_myprog.exe to the tempdir if needed here

        # Close the main application gracefully
        self.Destroy()
        wx.CallAfter(self.run_updater, fname)

    def run_updater(self, update_file):
        # Use subprocess to run the updater as a new process
        subprocess.Popen([update_file, '/SP-', '/silent', '/noicons', '/nocancel', '/password=pw'], 
                         creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
