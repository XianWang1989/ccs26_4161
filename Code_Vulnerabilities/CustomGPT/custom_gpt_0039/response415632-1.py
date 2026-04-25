
import wx
import os
import tempfile
import sys

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        canupdate = True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Download your update_myprog.exe to fname

            # Close the main application window
            self.Destroy()
            # Start the updater independently
            os.startfile(fname)
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
