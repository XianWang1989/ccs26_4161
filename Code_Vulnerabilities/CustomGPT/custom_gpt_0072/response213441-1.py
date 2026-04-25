
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(800, 600))

        # Bind the event to get the size after the window is shown
        self.Bind(wx.EVT_SIZE, self.on_size)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("light blue")

        self.Show()

    def on_size(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate the size in pixels (20% of width and height)
        panel_width = int(width * 0.20)
        panel_height = int(height * 0.20)

        # Resize the panel
        self.panel.SetSize(panel_width, panel_height)
        self.panel.Centre()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
