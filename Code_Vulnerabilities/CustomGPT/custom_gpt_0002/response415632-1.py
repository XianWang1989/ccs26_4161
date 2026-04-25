
import wx
import subprocess
import os
import sys
import tempfile
import ctypes

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton=wx.Button(self,label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON,self.update)

    def update(self,event):
        canupdate=True
        if canupdate:
            tempdir=tempfile.mkdtemp()
            fname=os.path.join(tempdir,'update_myprog.exe')
            # Assuming the update_myprog.exe is already downloaded at this location
            subprocess.Popen(fname, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
            self.Destroy()
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
