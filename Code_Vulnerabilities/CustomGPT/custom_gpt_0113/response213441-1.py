
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        # Get the screen size
        screen_size = wx.GetDisplaySize()

        # Calculate the width and height based on percentage
        width = int(screen_size[0] * 0.20)  # 20% of screen width
        height = int(screen_size[1] * 0.20)  # 20% of screen height

        super(Example, self).__init__(parent, title=title, size=(width, height))
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in Percentage')
    app.MainLoop()
