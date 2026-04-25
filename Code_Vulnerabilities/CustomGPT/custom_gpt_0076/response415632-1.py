
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
            # Download your update_myprog.exe to fname here
            # Example: requests.get(url, stream=True).content
            # Assume the update executable is already downloaded in the tempdir

            # Close the current application
            self.Destroy()
            sys.exit()  # Ensure the application exits before starting the updater

            # Run the update executable
            subprocess.call([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'])

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
