
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
        canupdate = True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')

            # Close the current program
            self.Destroy()

            # Start the update process
            updater_path = os.path.abspath(fname)
            subprocess.Popen([updater_path, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'], creationflags=subprocess.CREATE_NEW_CONSOLE)
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
