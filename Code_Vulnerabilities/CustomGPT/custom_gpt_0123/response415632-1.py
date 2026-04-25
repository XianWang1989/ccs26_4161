
import wx
import subprocess
import os
import tempfile
import sys

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')
        # Assuming you've downloaded update_myprog.exe to fname

        # Start update_myprog.exe in a new process
        subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'], 
                         creationflags=subprocess.CREATE_NO_WINDOW)

        # Close the current application
        self.Destroy()
        wx.CallAfter(sys.exit)

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
