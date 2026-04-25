
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Example of a size in percentage
        self.percent_size = (20, 20)

        # Convert percentage to pixel size
        self.pixel_size = self.percent_to_pixels(self.percent_size)

        self.SetSize(self.pixel_size)
        self.Show()

    def percent_to_pixels(self, percent_size):
        """Convert percentage sizes to pixels based on the frame size."""
        width, height = self.GetSize()
        pixel_width = int(width * (percent_size[0] / 100))
        pixel_height = int(height * (percent_size[1] / 100))
        return (pixel_width, pixel_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
