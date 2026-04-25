
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the screen size
        screen_width, screen_height = wx.GetDisplaySize()

        # Calculate the size based on percentages
        percentage_width = 0.2  # 20%
        percentage_height = 0.2  # 20%

        width = int(screen_width * percentage_width)
        height = int(screen_height * percentage_height)

        # Set the size using calculated pixel values
        self.SetSize((width, height))

        self.Centre()  # Center the window on the screen
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in Percentage')
    app.MainLoop()
