
import wx
import os
import sys
import win32api
import tempfile

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        # Create a temporary directory and prepare the updater executable
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Move the update_myprog.exe to the temp directory
        # Assuming `update_myprog.exe` is already downloaded and accessible
        # os.rename('path_to_downloaded_update_myprog.exe', fname)  # uncomment this line accordingly

        # Close the main program
        self.Destroy()

        # Use win32api to start the update without being a child process
        win32api.ShellExecute(0, "open", fname, '', '', 1)

        # Exit the main application
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
