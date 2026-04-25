
import os
import wx
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
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Start the updater using os.startfile instead of subprocess.Popen
            os.startfile("update_myprog.exe")
            self.Destroy()
            # Optionally delay exit to ensure the updater has a moment to start
            wx.CallAfter(sys.exit)  # This schedules the exit to happen after processing the current event

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
