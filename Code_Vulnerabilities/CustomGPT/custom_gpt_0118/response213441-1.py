
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the size of the screen
        screen_width, screen_height = wx.GetDisplaySize()

        # Define sizes in percentage
        width_percentage = 0.2  # 20%
        height_percentage = 0.2  # 20%

        # Convert percentages to pixels
        new_width = int(screen_width * width_percentage)
        new_height = int(screen_height * height_percentage)

        # Set the size of the frame
        self.SetSize((new_width, new_height))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
