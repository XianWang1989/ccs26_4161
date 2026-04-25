
import wx
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
            # Assuming update_myprog.exe has already been downloaded to fname
            os.startfile(fname)  # Use os.startfile to run the updater without a parent-child relationship
            self.Destroy()
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
