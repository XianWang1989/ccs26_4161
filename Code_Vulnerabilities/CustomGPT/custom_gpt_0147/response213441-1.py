
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get screen size
        screen_width, screen_height = wx.DisplaySize()

        # Calculate size based on a percentage of the screen size
        percentage_width = 0.20  # 20%
        percentage_height = 0.20  # 20%
        frame_width = int(screen_width * percentage_width)
        frame_height = int(screen_height * percentage_height)

        # Set frame size
        self.SetSize((frame_width, frame_height))
        self.Centre()  # Center the frame on the screen
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
