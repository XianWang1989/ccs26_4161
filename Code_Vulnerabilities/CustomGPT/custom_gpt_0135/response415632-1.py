
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

        # Ensure to copy the update executable to the temporary path
        # Replace this with your actual download code
        # shutil.copy("source_of_update_myprog.exe", fname)

        # Start the update executable as a detached process
        subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password=pw'],
                         creationflags=subprocess.DETACHED_PROCESS)
        # Close the original application
        self.Destroy()
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
