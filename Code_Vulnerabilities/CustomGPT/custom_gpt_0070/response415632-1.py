
import wx
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
        tempdir = tempfile.mkdtemp()
        update_path = os.path.join(tempdir, 'update_myprog.exe')

        # Download update_myprog.exe into update_path
        # Assume the download code is here

        # Close the current application
        self.Destroy()

        # Start the update executable
        os.startfile(update_path)  # This starts the executable independently
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
