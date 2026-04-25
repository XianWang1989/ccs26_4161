
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(800, 600))

        # Set size in percentage (e.g., 20% of width and height)
        self.SetSize(self.calculate_size_percentage(20, 20))

        self.Show()

    def calculate_size_percentage(self, width_percent, height_percent):
        # Get the current size of the window
        window_width, window_height = self.GetSize()

        # Calculate the new size in pixels
        new_width = int(window_width * (width_percent / 100))
        new_height = int(window_height * (height_percent / 100))

        return (new_width, new_height)


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percentage')
    app.MainLoop()
