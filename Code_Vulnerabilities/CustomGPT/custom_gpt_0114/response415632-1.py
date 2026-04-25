
import wx
import os
import tempfile
import sys
import win32api

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Assume update_myprog.exe is downloaded to fname        
        # Use os.startfile instead of subprocess to launch update_myprog.exe
        win32api.ShellExecute(0, 'open', fname, '/SP- /silent /noicons /nocancel /password="pw"', '', 0)

        # Close the application
        self.Destroy()
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
