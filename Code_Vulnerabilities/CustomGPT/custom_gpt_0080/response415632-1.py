
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
            # Create a temporary directory for the update executable
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')

            # Ensure to run the updater in a new command shell
            subprocess.Popen(f'start "" "{fname}" /SP- /silent /noicons /nocancel /password="pw"', shell=True)

            # Close the main program
            self.Destroy()
            wx.CallAfter(sys.exit)  # Ensure a clean exit

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
