
import wx
import subprocess
import os
import sys
import tempfile

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        canupdate = True
        if canupdate:
            # Create a temporary directory for the executable
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')

            # Download or copy your update_myprog.exe to fname here

            # Run the update executable without creating a child process
            subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'], 
                             creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

            # Close the main program
            self.Destroy()
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
