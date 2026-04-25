
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
        # Ensure all resources are saved and prepare for update
        self.Destroy()

        # Create a temporary directory for the update executable
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Download your update_myprog.exe here to fname (not shown)

        # Close the original program
        os._exit(0)  # Forcefully exit the program

        # Launch the update executable
        subprocess.Popen([fname], shell=True)
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
