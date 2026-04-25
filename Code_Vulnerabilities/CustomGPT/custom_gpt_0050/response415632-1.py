
import wx
import os
import sys
import tempfile
import subprocess

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
            # Here we need to copy the update executable to temp directory
            # Ensure the file is downloaded properly here as an example
            # os.rename("downloaded_path/update_myprog.exe", fname) 

            # Launching the updater without being a child process
            subprocess.Popen([fname, "/SP-", "/silent", "/noicons", "/nocancel", "/password=pw"], shell=True)

            # Close the main application
            self.Destroy()
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
