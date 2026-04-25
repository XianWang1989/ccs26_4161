
import os
import sys
import wx
import subprocess
import win32process
import tempfile

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
            # Download / copy the update_myprog.exe to the tempdir
            # For the sake of example, we assume this file is already in the tempdir

            # Close the application gracefully
            self.Destroy()
            wx.CallAfter(self.run_updater, fname)

    def run_updater(self, updater_path):
        # Launch the updater executable
        # Set the `creationflags` to DETACHED_PROCESS
        win32process.CreateProcess(
            updater_path,
            None,
            None,
            None,
            0,
            win32process.DETACHED_PROCESS,
            None,
            None
        )
        # Exit the current application
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
