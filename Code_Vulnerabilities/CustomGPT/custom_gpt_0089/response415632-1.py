
import wx
import ctypes
import sys
import os
import tempfile

class Main(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('MyProg v1')
        self.updatebutton = wx.Button(self, label='Update')
        self.updatebutton.Bind(wx.EVT_BUTTON, self.update)

    def update(self, event):
        tempdir = tempfile.mkdtemp()
        fname = os.path.join(tempdir, 'update_myprog.exe')

        # Path to your update executable
        update_exe = os.path.abspath("update_myprog.exe")

        # Use ctypes to run the update executable in a separate process
        ctypes.windll.kernel32.CreateProcessW(
            update_exe, 
            None, 
            None, 
            None, 
            False, 
            0, 
            None, 
            None, 
            ctypes.byref(ctypes.wintypes.STARTUPINFO())
        )

        # Close the existing application
        self.Destroy()
        sys.exit()

app = wx.App(False)
Main(parent=None).Show(True)
app.MainLoop()
