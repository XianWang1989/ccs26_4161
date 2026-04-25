
import wx
import os
import tempfile
import subprocess
import sys

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
            # Here you would normally download the update_myprog.exe file
            # For example, using requests.get() and saving it

            # Use os.startfile instead of subprocess.Popen
            os.startfile(fname)

            self.Destroy()
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
