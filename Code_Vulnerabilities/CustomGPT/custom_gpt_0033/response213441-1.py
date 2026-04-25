
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Bind the size event to calculate percentage sizes
        self.Bind(wx.EVT_SIZE, self.on_size)

        self.panel = wx.Panel(self)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))  # Set background color for visibility

        self.Show()

    def on_size(self, event):
        width, height = self.GetSize()

        # Calculate sizes based on percentage
        width_percent = int(width * 0.2)  # 20%
        height_percent = int(height * 0.2)  # 20%

        # Set the size and position of the panel based on percentages
        self.panel.SetSize((width_percent, height_percent))
        self.panel.SetPosition((width - width_percent, height - height_percent))  # Position it in the bottom right

        event.Skip()  # Continue with default handling

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
