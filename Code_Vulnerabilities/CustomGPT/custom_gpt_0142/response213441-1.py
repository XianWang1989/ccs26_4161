
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the size of the screen
        screen_width, screen_height = wx.GetDisplaySize()

        # Calculate size as a percentage of the screen size
        width = int(screen_width * 0.2)  # 20% of screen width
        height = int(screen_height * 0.2)  # 20% of screen height

        # Set the size of the frame
        self.SetSize((width, height))
        self.Center()  # Center the frame on the screen
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
