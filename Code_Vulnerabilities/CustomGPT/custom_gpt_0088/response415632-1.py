
import os
import sys
import wx
import subprocess
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

            # Copy the downloaded updater to temp
            # shutil.copy('path_to_downloaded_update_myprog.exe', fname)

            # Start the updater process
            subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'])

            # Close the current app
            self.Destroy()
            wx.CallAfter(sys.exit)

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
