
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the screen dimensions
        screen_width, screen_height = wx.GetDisplaySize()

        # Calculate 20% of screen dimensions
        width = int(screen_width * 0.2)  # 20% width
        height = int(screen_height * 0.2)  # 20% height

        # Set the size of the window
        self.SetSize((width, height))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
