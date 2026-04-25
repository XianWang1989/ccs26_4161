
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(400, 300))

        # Bind the size event to calculate sizes
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.panel = wx.Panel(self)

        self.Show()

    def OnSize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate the size based on percentage
        panel_width = int(width * 0.2)  # 20% of frame width
        panel_height = int(height * 0.2)  # 20% of frame height

        # Set size of the panel
        self.panel.SetSize(panel_width, panel_height)
        self.panel.SetBackgroundColour(wx.Colour(100, 100, 250))

        # Layout the panel
        self.Layout()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
