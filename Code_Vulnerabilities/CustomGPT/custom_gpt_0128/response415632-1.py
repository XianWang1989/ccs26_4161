
import wx
import subprocess
import os
import sys
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

            # Ensure the full path to the update executable
            update_executable = os.path.abspath(fname)

            # Start the updater, ensuring to detach it from the current process
            subprocess.Popen(update_executable, creationflags=subprocess.DETACHED_PROCESS)
            self.Destroy()
            sys.exit()  # Ensure the original program exits

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
