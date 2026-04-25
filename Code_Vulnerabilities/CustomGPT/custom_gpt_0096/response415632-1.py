
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
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Make sure to specify the correct path for update_myprog.exe
        subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'], 
                         creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

        # Close the main application
        self.Destroy()
        wx.CallAfter(sys.exit)  # Ensures the wx app exits after the subprocess starts

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
