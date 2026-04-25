
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the size of the window
        self.Bind(wx.EVT_SIZE, self.OnResize)
        self.Show()

    def OnResize(self, event):
        size = self.GetSize()

        # Calculate sizes as percentages
        width_percentage = int(size[0] * 0.2)  # 20% of the current width
        height_percentage = int(size[1] * 0.2)  # 20% of the current height

        # Set the size of a panel or other child widget
        self.SetSize((width_percentage, height_percentage))

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
