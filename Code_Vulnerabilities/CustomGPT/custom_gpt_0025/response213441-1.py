
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the screen size
        screen_width, screen_height = wx.GetDisplaySize()

        # Convert percentage to pixel size
        width_percentage = 0.2  # 20%
        height_percentage = 0.2  # 20%

        width = int(screen_width * width_percentage)
        height = int(screen_height * height_percentage)

        # Set the size of the frame using calculated pixel values
        self.SetSize((width, height))

        # Show the frame
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
