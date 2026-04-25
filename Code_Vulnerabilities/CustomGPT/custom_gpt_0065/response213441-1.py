
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the screen size
        screen_width, screen_height = wx.GetDisplaySize()

        # Calculate the size in pixels (20% of screen size)
        width = int(screen_width * 0.2)  # 20% width
        height = int(screen_height * 0.2)  # 20% height

        self.SetSize((width, height))  # Set the calculated size
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
