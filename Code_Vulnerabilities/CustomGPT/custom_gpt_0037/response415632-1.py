
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
        canupdate = True  # Replace with actual logic if needed
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')

            # Launch the update process and detach it
            update_process = subprocess.Popen(
                [fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'],
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
                close_fds=True
            )

            # Close the current application
            self.Destroy()
            wx.CallAfter(lambda: sys.exit())  # Ensures the application exits after closing the frame

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
