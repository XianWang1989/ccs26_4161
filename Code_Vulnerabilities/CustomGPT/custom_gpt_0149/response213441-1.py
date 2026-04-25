
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(800, 600))

        # Get window size
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(200, 200, 255))

        self.Show()

    def on_resize(self, event):
        # Get the size of the window
        width, height = self.GetSize()

        # Calculate sizes as percentages
        panel_width = int(width * 0.20)  # 20% of width
        panel_height = int(height * 0.20)  # 20% of height

        # Resize the panel
        self.panel.SetSize(panel_width, panel_height)

        event.Skip()  # Allow other events to process

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
