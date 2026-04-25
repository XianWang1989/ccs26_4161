
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Bind the size event to update layout on resize
        self.Bind(wx.EVT_SIZE, self.on_size)

        # Create a panel
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        # Initially draw layout
        self.on_size()

        self.Show()

    def on_size(self, event=None):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate sizes based on percentage
        panel_width = int(width * 0.2)  # 20%
        panel_height = int(height * 0.2)  # 20%

        # Resize panel
        self.panel.SetSize(panel_width, panel_height)
        self.panel.Centre()  # Center the panel

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
