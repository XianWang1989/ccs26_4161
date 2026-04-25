
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
        canupdate = True
        if canupdate:
            tempdir = tempfile.mkdtemp()
            update_path = os.path.join(tempdir, 'update_myprog.exe')
            # Copy your update_myprog.exe to tempdir here, this is just an example placeholder
            # shutil.copy("path_to_update_myprog.exe", update_path)

            # Close the application
            self.Destroy()
            # Run the updater without it being a child process
            os.startfile(update_path)
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
