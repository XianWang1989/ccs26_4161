
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

        # Copy the downloader executable to the temp directory
        # (Add code here to download and save update_myprog.exe to fname)

        # Start the updater and exit the main app
        subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'])
        self.Destroy()
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
