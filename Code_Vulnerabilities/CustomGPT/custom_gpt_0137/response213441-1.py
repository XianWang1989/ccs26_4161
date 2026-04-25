
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(600, 400))

        # Create a panel with a specified size in pixels
        # Convert percentage to pixel size
        panel_size_x = int(self.GetSize().width * 0.2)  # 20% of frame width
        panel_size_y = int(self.GetSize().height * 0.2)  # 20% of frame height

        self.panel = wx.Panel(self, size=(panel_size_x, panel_size_y))
        self.panel.SetBackgroundColour(wx.Colour(255, 0, 0))  # Set panel background to red

        self.Layout()  # Ensure layout updates to reflect any size changes
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
