
import os
import sys
import wx
import tempfile

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.bat')

        # Create a batch file to run the update exe
        with open(fname, 'w') as f:
            f.write(f'@echo off\n')
            f.write(f'start /wait update_myprog.exe /SP- /silent /noicons /nocancel /password="pw"\n')
            f.write(f'del "%~f0"\n')  # Delete the batch file after execution

        self.Destroy()  # Close the main application
        os.startfile(fname)  # Run the batch file
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
