
import os
import sys
import wx
import subprocess
import tempfile

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton=wx.Button(self,label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON,self.update)

    def update(self,event):
        # Create a temporary directory for the update
        tempdir = tempfile.mkdtemp()
        # Path to the update executable
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Assume the update_myprog.exe is already downloaded to fname

        # Close the current application
        self.Destroy()

        # Call the update, ensuring it's not a child process
        os.startfile(fname)  # This will start update_myprog.exe independently

        # Exit the current program
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
