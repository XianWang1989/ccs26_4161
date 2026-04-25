
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
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Use subprocess to run the updater without it being a child process
        subprocess.Popen(
            [fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'],
            creationflags=win32process.CREATE_NEW_CONSOLE | win32process.CREATE_NEW_PROCESS_GROUP
        )

        # Close the current program
        self.Destroy()
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
