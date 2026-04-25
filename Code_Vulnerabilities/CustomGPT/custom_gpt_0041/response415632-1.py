
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
            tempdir = tempfile.mkdtemp()
            exe_path = os.path.join(tempdir, 'update_myprog.exe')

            # Move the update executable to the temp directory for updating
            # (Assuming the file is already downloaded to this location)
            # os.rename(downloaded_file_path, exe_path)

            # Close the current application and run the update
            self.Destroy()

            # Launch the update executable
            os.startfile(exe_path)  # Use os.startfile to run the updater
            sys.exit(0)  # Ensure the original application exits

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
