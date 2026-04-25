
import wx
import os
import sys
import tempfile
import subprocess

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Download or copy your update executable to fname
        # For demonstration, we'll assume it's already there...

        # Close the current application
        self.Destroy()  # Close the wx Frame
        wx.CallAfter(sys.exit)  # Schedule the exit after the frame is closed

        # Run the update executable without inheriting the parent process
        subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'], 
                         creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS)

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
