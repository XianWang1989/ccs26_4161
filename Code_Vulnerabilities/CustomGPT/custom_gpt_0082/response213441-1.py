
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(400, 300))

        self.Bind(wx.EVT_SIZE, self.OnResize)

        # Initial layout
        self.panel = wx.Panel(self)
        self.SetSizePercentage(20, 20)  # Set size to 20% of the frame

        self.Show()

    def SetSizePercentage(self, width_percent, height_percent):
        size = self.GetSize()
        new_width = int(size[0] * (width_percent / 100))
        new_height = int(size[1] * (height_percent / 100))
        self.panel.SetSize((new_width, new_height))
        self.panel.SetBackgroundColour(wx.Colour(200, 200, 255))  # Just for visualization

    def OnResize(self, event):
        # Resize the panel according to the new frame size
        self.SetSizePercentage(20, 20)
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
