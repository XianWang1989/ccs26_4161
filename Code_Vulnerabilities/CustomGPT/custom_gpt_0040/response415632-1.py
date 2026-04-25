
import wx
import win32api
import os
import tempfile
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

            # Use ShellExecute to run the updater independently
            win32api.ShellExecute(0, "open", fname, "/SP- /silent /noicons /nocancel /password=pw", None, 1)

            self.Destroy()
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
