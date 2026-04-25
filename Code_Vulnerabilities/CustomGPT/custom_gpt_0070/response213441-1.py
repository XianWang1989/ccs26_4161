
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Bind the size event to calculate percentages
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("light grey")

        self.Show()

    def OnSize(self, event):
        # Get current size of the window
        width, height = self.GetSize()

        # Calculate sizes in percentage (20% of width and height)
        new_width = int(width * 0.20)
        new_height = int(height * 0.20)

        # Set a new size for the panel based on calculated percentages
        self.panel.SetSize(new_width, new_height)
        self.Layout()  # Re-layout the frame

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size Example')
    app.MainLoop()
