
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get screen size
        screen_width, screen_height = wx.GetDesktopSize()

        # Define desired size as percentages
        width_percentage = 0.2  # 20%
        height_percentage = 0.2  # 20%

        # Calculate actual size in pixels
        width = int(screen_width * width_percentage)
        height = int(screen_height * height_percentage)

        # Set the size of the frame
        self.SetSize((width, height))

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
