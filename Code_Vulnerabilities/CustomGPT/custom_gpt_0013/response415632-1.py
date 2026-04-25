
import wx
import subprocess
import sys
import os
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
        # Download your update_myprog.exe here and save it to fname
        # For demonstration, we are assuming it is already there

        # Launch the updater and ensure the current application exits
        subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'], shell=True)
        self.Destroy()
        sys.exit()  # Ensures the original application closes

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
