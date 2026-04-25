
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
        fname = os.path.join(tempdir, 'update_myprog.exe')
        # Download/update the update_myprog.exe here if needed
        # e.g., requests.get(url, stream=True).content stored into fname

        # Close the current application and run the updater
        self.Destroy()
        os.execv(fname, [fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'])

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
