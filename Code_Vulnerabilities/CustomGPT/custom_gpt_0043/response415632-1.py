
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
            fname = os.path.join(tempdir, 'update_myprog.exe')
            # Make sure we copy the actual update executable here
            # e.g., download it to fname
            # For this example, we'll assume it's already available
            subprocess.Popen([fname, '/SP-', '/silent', '/noicons', '/nocancel', '/password="pw"'], 
                             creationflags=subprocess.CREATE_NEW_CONSOLE)
            self.Destroy()  # Close the main application
            sys.exit()      # Exit the program completely

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
