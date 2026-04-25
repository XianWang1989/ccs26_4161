
import wx
import os
import tempfile
import sys
import time

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        canupdate = True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')

            # Assuming 'update_myprog.exe' is already downloaded to the temp directory here
            # You would download it before calling the update
            # os.rename(downloaded_path, fname)  # Example of renaming/moving downloaded file

            # Close the application
            self.Destroy()
            time.sleep(1)  # Give it a moment to close the GUI

            # Start the update executable
            os.startfile(fname)  # This opens the file independently

            # Exit the original application
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
