
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the display size
        screen_width, screen_height = wx.GetDisplaySize()

        # Set size in percentage
        width = int(screen_width * 0.20)  # 20%
        height = int(screen_height * 0.20)  # 20%

        self.SetSize((width, height))
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
