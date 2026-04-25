
import os
import sys
import wx
import subprocess
import win32process
import tempfile

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

            # Download or copy update_myprog.exe to fname here
            # For example: shutil.copy('source_path', fname)

            # Create the command without quotes
            cmd = [fname, "/SP-", "/silent", "/noicons", "/nocancel", '/password="pw"']
            # Run it as a detached process
            win32process.CreateProcess(
                None, 
                ' '.join(cmd), 
                None, 
                None, 
                False, 
                win32process.CREATE_NEW_PROCESS_GROUP | win32process.CREATE_NO_WINDOW, 
                None, 
                None
            )
            self.Destroy()
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
