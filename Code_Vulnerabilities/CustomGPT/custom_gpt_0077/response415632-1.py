
import wx
import subprocess
import time
import os
import sys

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        canupdate = True
        if canupdate:
            update_path = "update_myprog.exe"
            # Ensure the main loop is exited
            self.Destroy()
            time.sleep(1)  # Short delay to allow the GUI to close properly
            # Use os.startfile to run the update without it being a child process
            os.startfile(update_path)
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
