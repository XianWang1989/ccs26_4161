
import wx
import subprocess
import os
import sys
import tempfile
import win32api
import time

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton=wx.Button(self,label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON,self.update)

    def update(self, event):
        canupdate=True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Ensure the original program is closed
            win32api.TerminateProcess(win32process.GetCurrentProcess(), 0)  # Terminate process forcefully
            time.sleep(0.5)  # Allow some time for the termination to complete

            # Start the updater
            os.startfile(fname)  # Using os.startfile for better detachment
            sys.exit()  # Exit the original application

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
