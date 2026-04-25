
import wx
import subprocess
import os
import sys
import tempfile

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        # Program logic for update
        canupdate = True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Download your update_myprog.exe file to fname here if necessary
            # For demonstration, let's say we just take it from current directory
            # Assume that our update_myprog.exe exists in the same directory
            update_exe = os.path.join(os.getcwd(), "update_myprog.exe")
            # Close the current wxPython app using sys.exit after firing the updater
            self.Destroy()  # Destroy the GUI frame
            # Use os.startfile to make it a separate process
            os.startfile(update_exe)
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
