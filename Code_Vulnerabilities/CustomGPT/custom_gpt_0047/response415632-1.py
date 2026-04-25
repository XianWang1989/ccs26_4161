
import wx
import os
import tempfile
import sys
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
            # Download or copy your update_myprog.exe to fname
            # For demonstration, assume it's already there.

            # Prepare command
            command = f'"{fname}" /SP- /silent /noicons /nocancel /password="pw"'

            # Close current app
            self.Destroy()  # Close current frame
            app.ExitMainLoop()  # Exit the main loop

            # Use os.startfile for running the updater
            os.startfile(fname)

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
