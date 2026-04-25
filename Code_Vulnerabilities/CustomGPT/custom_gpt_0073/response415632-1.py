
import wx
import os
import tempfile
import sys
import time

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton=wx.Button(self,label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON,self.update)

    def update(self,event):
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Assume you've already downloaded the update_myprog.exe to `fname`.
        # Launch the updater using os.startfile
        os.startfile(fname)

        # Allow some time for the new process to start
        time.sleep(1)

        # Close the current application
        self.Destroy()
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
