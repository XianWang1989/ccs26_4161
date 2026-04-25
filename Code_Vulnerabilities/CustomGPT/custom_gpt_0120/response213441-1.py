
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set the frame size based on percentages
        self.SetInitialSize(self.calculate_percentage_size(20, 20))

        self.Show()

    def calculate_percentage_size(self, width_percentage, height_percentage):
        # Get the screen size
        screen_width, screen_height = wx.GetDisplaySize()

        # Calculate the desired size in pixels
        width = int(screen_width * (width_percentage / 100))
        height = int(screen_height * (height_percentage / 100))

        return (width, height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
