
import wx
import os
import tempfile
import sys
import win32api

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton=wx.Button(self,label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON,self.update)

    def update(self,event):
        canupdate=True
        if(canupdate):
            # This is where you would download your update_myprog.exe to a temp directory
            tempdir=tempfile.gettempdir()
            fname=os.path.join(tempdir,'update_myprog.exe')
            # Assuming you've previously downloaded update_myprog.exe to fname

            # Close the running application
            self.Destroy()  # Closes the wxPython frame
            win32api.ShellExecute(0, 'open', fname, None, None, 1)  # Starts the update installer
            sys.exit()  # Terminate the current Python process

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
