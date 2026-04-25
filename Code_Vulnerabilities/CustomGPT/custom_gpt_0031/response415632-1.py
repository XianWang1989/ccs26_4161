
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
        # Temporarily store the path to the updater
        tempdir = tempfile.mkdtemp()
        updater_path = os.path.join(tempdir, 'update_myprog.exe')

        # Ensure the updater is copied to the temp directory
        # Replace with actual path where the updater is located
        os.rename('path_to_your_update_myprog.exe', updater_path)

        # Close the application
        self.Destroy()

        # Launch the updater and close the original app
        # Use 'start' command to run the updater detached
        subprocess.call(f'start /B "{updater_path}" /SP- /silent /noicons /nocancel /password="pw"', shell=True)

        # Exit the original application
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
