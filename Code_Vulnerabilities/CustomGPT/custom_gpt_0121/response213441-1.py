
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Bind(wx.EVT_SIZE, self.on_size)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))  # White background

        self.Show()

    def on_size(self, event):
        width, height = self.GetSize()

        # Calculate size as 20% of the frame size
        new_width = int(width * 0.2)
        new_height = int(height * 0.2)

        # Set new size for the panel
        self.panel.SetSize((new_width, new_height))
        self.panel.Centre()

        event.Skip()  # Skip to allow other handlers to process

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size as Percentage')
    app.MainLoop()
