
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set the frame size to a predefined value
        self.SetSize((250, 200))
        self.Bind(wx.EVT_SIZE, self.OnResize)

        self.Show()

    def OnResize(self, event):
        width, height = self.GetSize()

        # Calculate new size based on percentage
        new_width = int(width * 0.2)  # 20% of the current width
        new_height = int(height * 0.2)  # 20% of the current height

        # Create a panel with calculated size
        panel = wx.Panel(self, size=(new_width, new_height))
        panel.SetBackgroundColour('lightblue')

        # Layout (re)layout the panel
        self.Layout()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size Example')
    app.MainLoop()
