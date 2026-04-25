
import wx
import subprocess
import win32process
import tempfile
import os

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
            fname = os.path.join(tempdir, 'update_myprog.exe')  # Adjust if downloading
            # Correctly detach the process
            proc = subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'], 
                                    creationflags=win32process.DETACHED_PROCESS)
            self.Destroy()
            os._exit(0)  # Forcefully exit the original program

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
