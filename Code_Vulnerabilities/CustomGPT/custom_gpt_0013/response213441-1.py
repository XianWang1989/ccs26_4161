
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get screen size
        screen_size = wx.GetDisplaySize()

        # Calculate size in pixels based on percentage
        width_percentage = 0.2  # 20%
        height_percentage = 0.2  # 20%

        width = int(screen_size[0] * width_percentage)
        height = int(screen_size[1] * height_percentage)

        self.SetSize((width, height))
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
