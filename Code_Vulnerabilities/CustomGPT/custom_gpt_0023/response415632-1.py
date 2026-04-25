
import wx
import subprocess
import os
import tempfile
import sys
import time

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        # Prepare temporary directory and filename
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Path to the updater executable
        updater_path = os.path.abspath('update_myprog.exe')

        # Close the application cleanly
        self.Destroy()

        # Wait a moment to ensure all resources are released
        time.sleep(0.5)

        # Start the updater process
        subprocess.Popen(updater_path, creationflags=subprocess.CREATE_NEW_CONSOLE)

        # Exit the main application
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
