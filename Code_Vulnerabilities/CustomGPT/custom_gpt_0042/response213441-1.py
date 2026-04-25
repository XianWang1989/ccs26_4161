
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get screen size
        screen_width = wx.GetDisplaySize()[0]
        screen_height = wx.GetDisplaySize()[1]

        # Set the size in percentage (20% width, 20% height)
        width = int(screen_width * 0.2)
        height = int(screen_height * 0.2)

        self.SetSize((width, height))
        self.Center()  # Center the frame on the screen
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
