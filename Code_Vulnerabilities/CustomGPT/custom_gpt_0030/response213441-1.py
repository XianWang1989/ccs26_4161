
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Bind(wx.EVT_SIZE, self.on_size)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))  # Set a background color

        self.Show()

    def on_size(self, event):
        width, height = self.GetSize()

        # Calculate size based on percentages
        new_width = int(width * 0.2)  # 20% of the frame width
        new_height = int(height * 0.2)  # 20% of the frame height

        # Set the size of the panel
        self.panel.SetSize(new_width, new_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
