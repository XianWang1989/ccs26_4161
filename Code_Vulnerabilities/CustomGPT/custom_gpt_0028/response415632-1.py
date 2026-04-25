
import wx
import os
import subprocess
import threading
import tempfile
import time

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Assuming you downloaded the update_myprog.exe to fname

        # Start the update process
        threading.Thread(target=self.run_updater, args=(fname,)).start()

    def run_updater(self, updater_path):
        # Start the update program
        os.startfile(updater_path)
        # Sleep for a short duration to ensure the updater starts
        time.sleep(1)
        # Close the main application
        self.Destroy()
        wx.CallAfter(wx.Exit)

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
