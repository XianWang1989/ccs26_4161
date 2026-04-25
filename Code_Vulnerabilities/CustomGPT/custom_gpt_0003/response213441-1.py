
# -*- coding: utf-8 -*-

# size.py

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the screen size
        screen_width, screen_height = wx.GetDisplaySize()

        # Define the size as a percentage for the width and height
        width_percentage = 0.20  # 20%
        height_percentage = 0.20  # 20%

        # Calculate the new size in pixels
        new_width = int(screen_width * width_percentage)
        new_height = int(screen_height * height_percentage)

        # Set the size based on the calculated pixel values
        self.SetSize((new_width, new_height))

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
