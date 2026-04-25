
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get screen size
        screen_size = wx.GetDisplaySize()
        width_percent = 0.2  # 20%
        height_percent = 0.2  # 20%

        # Calculate size in pixels
        width = int(screen_size[0] * width_percent)
        height = int(screen_size[1] * height_percent)

        # Set the size based on calculated dimensions
        self.SetSize((width, height))
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
