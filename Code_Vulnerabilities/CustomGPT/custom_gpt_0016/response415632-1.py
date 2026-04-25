
import wx
import os
import tempfile
import shutil
import sys

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        # Assuming you have already downloaded update_myprog.exe to a temporary location
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Here, you'd normally download the update_myprog.exe to `fname`.
        # For example's sake, we'll assume it's done successfully.

        # Schedule the update process to run independently
        os.startfile(fname)  # Executes the updater independently

        # Ensure the main program closes
        self.Destroy()
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
