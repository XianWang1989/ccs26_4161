
import wx
import subprocess
import win32api
import tempfile
import os
import sys

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton=wx.Button(self,label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON,self.update)

    def update(self, event):
        canupdate = True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')

            # Download your update_myprog.exe to fname here

            # Close the application
            self.Destroy()
            wx.CallAfter(self.run_updater, fname)

    def run_updater(self, updater_path):
        # Run the updater as a new process
        subprocess.Popen([updater_path, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'], 
                         creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
