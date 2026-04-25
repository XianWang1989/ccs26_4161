
import os
import sys
import wx
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
            # Download and prepare the update executable here
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Here you should have code to download the update_myprog.exe

            # Instead of Popen, use os.startfile to avoid parent-child process linkage
            os.startfile(fname)

            # Close the current application
            self.Destroy()
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
