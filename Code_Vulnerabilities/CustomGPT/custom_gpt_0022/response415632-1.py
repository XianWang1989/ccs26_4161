
import wx
import os
import sys
import tempfile
import win32api

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        # Assume the update file is downloaded and ready
        update_path = os.path.join(os.getcwd(), 'update_myprog.exe')

        # Close the current application
        self.Destroy()

        # Execute the update application
        win32api.ShellExecute(0, "open", update_path, '/SP- /silent /noicons /nocancel /password="pw"', None, 1)

        # Exit the current application
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
