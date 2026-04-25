
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
        canupdate = True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Start the update executable using subprocess
            process = subprocess.Popen(
                [fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            self.Destroy()  # Close the app
            sys.exit()  # Exit the program

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
