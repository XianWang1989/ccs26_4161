
import wx
import subprocess
import sys
import os
import tempfile
import time

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
            # Move the update executable to the temp dir
            # (Ensure that this is the actual path where it is downloaded)
            # Example: shutil.copy("path_to_downloaded_update_exe", fname)

            # Close the application first
            self.Destroy()
            time.sleep(1)  # Allow time to ensure frame is really closed

            # Now run the updater
            subprocess.Popen(fname, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
