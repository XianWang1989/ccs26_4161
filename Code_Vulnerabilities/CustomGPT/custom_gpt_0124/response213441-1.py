
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set size using percentage of parent size
        self.SetSize(self.calculate_size(0.2, 0.2))
        self.Show()

    def calculate_size(self, width_percent, height_percent):
        screen_size = wx.GetDisplaySize()  # Get screen size
        width = int(screen_size[0] * width_percent)
        height = int(screen_size[1] * height_percent)
        return (width, height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
