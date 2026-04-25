
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Set layout sizes in percentage
        self.SetSizeToPercentage(20, 20)  # 20% width and height

        self.Show()

    def SetSizeToPercentage(self, width_percent, height_percent):
        # Get the current screen size
        screen_width, screen_height = wx.GetDisplaySize()

        # Calculate the size in pixels
        width = int(screen_width * (width_percent / 100))
        height = int(screen_height * (height_percent / 100))

        # Set the size
        self.SetSize(width, height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
