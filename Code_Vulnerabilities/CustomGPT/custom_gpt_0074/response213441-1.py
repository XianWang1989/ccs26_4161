
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the screen size to calculate percentages
        screen_width, screen_height = wx.GetDisplaySize()

        # Define your desired size in percentage
        width_percentage = 20  # 20% of the screen width
        height_percentage = 20  # 20% of the screen height

        # Convert percentage to pixels
        width_pixels = int(screen_width * (width_percentage / 100))
        height_pixels = int(screen_height * (height_percentage / 100))

        # Set the size using the calculated pixel values
        self.SetSize((width_pixels, height_pixels))

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
