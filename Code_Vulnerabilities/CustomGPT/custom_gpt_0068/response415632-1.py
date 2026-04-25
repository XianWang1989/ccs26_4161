
import wx
import subprocess
import os
import tempfile
import time

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        # Ensure the update is allowed
        canupdate = True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Start the update executable
            proc = subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'])
            # Allow some time for the subprocess to start
            time.sleep(1)
            # Close the application
            self.Destroy()
            os._exit(0)  # Use os._exit to ensure the interpreter exits immediately

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
