
import wx
import subprocess
import win32process
import tempfile
import os
import sys

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        # Create a temporary file path for the update executable
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Move your update executable to temp dir (if needed)
        # shutil.copy('update_myprog.exe', fname)

        # Create a batch file to handle the update
        batch_file_path = os.path.join(tempdir, 'update.bat')
        with open(batch_file_path, 'w') as f:
            f.write(f"taskkill /F /IM {os.path.basename(sys.executable)}\n")
            f.write(f'start "" "{fname}"\n')
            f.write('exit\n')

        # Run the batch file
        subprocess.Popen(batch_file_path, creationflags=win32process.DETACHED_PROCESS)
        self.Destroy()
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
