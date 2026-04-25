
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
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Assuming you have already downloaded update_myprog.exe to 'fname'
        # Now execute the update without making it a child process
        self.Destroy()  # Close the current window before calling sys.exit()
        subprocess.Popen([fname], creationflags=subprocess.CREATE_NEW_CONSOLE)  # Run the update
        sys.exit()  # Ensure the original program exits

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
