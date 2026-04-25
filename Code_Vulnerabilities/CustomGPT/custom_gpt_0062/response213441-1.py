
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the screen size
        screen_width, screen_height = wx.GetScreenSize()

        # Calculate the size in pixels based on percentage
        width = int(screen_width * 0.2)  # 20%
        height = int(screen_height * 0.2)  # 20%

        # Set the size in pixels
        self.SetSize((width, height))
        self.Center()  # Center the window on the screen

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
