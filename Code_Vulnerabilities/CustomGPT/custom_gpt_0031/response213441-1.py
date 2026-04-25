
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set initial size of the frame
        self.SetSize(800, 600)  # Example defined window size

        # Get the size of the window
        width, height = self.GetSize()

        # Convert percentage to pixels
        percent_width = int(width * 0.2)  # 20% of the total width
        percent_height = int(height * 0.2)  # 20% of the total height

        # Create a panel with specified size in pixels
        panel = wx.Panel(self, size=(percent_width, percent_height))
        panel.SetBackgroundColour(wx.Colour(255, 255, 255))  # White background

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in Percentage')
    app.MainLoop()
