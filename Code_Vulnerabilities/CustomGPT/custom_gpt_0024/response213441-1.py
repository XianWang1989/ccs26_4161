
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the screen size in pixels
        screen_width, screen_height = wx.GetDisplaySize()

        # Calculate width and height as percentages
        width_percentage = 0.20  # 20%
        height_percentage = 0.20  # 20%

        # Convert percentages to pixels
        width = int(screen_width * width_percentage)
        height = int(screen_height * height_percentage)

        # Set the size using the calculated pixel values
        self.SetSize((width, height))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in Percent')
    app.MainLoop()
