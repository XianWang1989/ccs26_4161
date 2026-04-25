
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Get the size of the frame to calculate percentages
        self.Bind(wx.EVT_SIZE, self.on_size)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.Show()

    def on_size(self, event):
        width, height = self.GetSize()

        # Define sizes as percentages
        percent_width = 0.20  # 20%
        percent_height = 0.20  # 20%

        # Calculate pixel sizes
        size_width = int(width * percent_width)
        size_height = int(height * percent_height)

        # Create a button with calculated size
        self.button = wx.Button(self.panel, label="Click Me", size=(size_width, size_height))
        self.button.Center()  # Center the button on the panel
        self.panel.Layout()  # Refresh the layout

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size Example')
    app.MainLoop()
