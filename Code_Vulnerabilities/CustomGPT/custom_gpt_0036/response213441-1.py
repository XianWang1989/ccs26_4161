
# -*- coding: utf-8 -*-

# size.py

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Bind(wx.EVT_SIZE, self.OnResize)  # Bind the resize event
        self.Show()

    def OnResize(self, event):
        # Get the size of the frame
        width, height = self.GetSize()

        # Calculate the desired sizes in pixels based on a percentage
        desired_width = int(0.2 * width)  # 20%
        desired_height = int(0.2 * height)  # 20%

        # Setting a child panel with a size based on percentage
        panel = wx.Panel(self)
        panel.SetSize(desired_width, desired_height)

        # Optional: Center the panel
        panel.Centre(wx.BOTH)

        # Refresh the layout
        self.Layout()

if __name__ == '__main__':
    app = wx.App(False)
    Example(None, title='Size')
    app.MainLoop()
