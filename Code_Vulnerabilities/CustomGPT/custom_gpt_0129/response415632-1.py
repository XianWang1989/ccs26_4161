
import os
import wx
import subprocess
import tempfile
import sys

class Main(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton=wx.Button(self,label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON,self.update)

    def update(self,event):
        canupdate = True
        if (canupdate):
            tempdir = tempfile.mkdtemp()
            fname = os.path.join(tempdir, 'update_myprog.exe')

            # Create a batch file to run the update
            batch_file_content = f'@echo off\nstart "" "{os.path.join(tempdir, "update_myprog.exe")}"\nexit'
            batch_file_path = os.path.join(tempdir, 'run_update.bat')

            with open(batch_file_path, 'w') as batch_file:
                batch_file.write(batch_file_content)

            # Run the batch file
            subprocess.Popen([batch_file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)

            # Clean exit
            self.Destroy()
            sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
