
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set frame size to 80% of the screen size
        screen_width = wx.GetDisplaySize()[0]
        screen_height = wx.GetDisplaySize()[1]
        width = int(screen_width * 0.8)  # 80% of screen width
        height = int(screen_height * 0.8)  # 80% of screen height

        self.SetSize((width, height))
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
