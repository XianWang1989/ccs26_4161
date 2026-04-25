
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Calculate size in pixels from percentages
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.Show()

    def on_resize(self, event):
        # Get the current size of the window
        width, height = self.GetSize()

        # Calculate desired sizes as 20% of the window size
        panel_size = (int(0.2 * width), int(0.2 * height))

        # Resize the panel
        self.panel.SetSize(panel_size)
        self.Layout()  # Refresh layout


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percentages')
    app.MainLoop()
