
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Bind the size event to dynamically calculate sizes
        self.Bind(wx.EVT_SIZE, self.on_size)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(200, 200, 200))

        self.Show()

    def on_size(self, event):
        # Get the size of the frame
        width, height = self.GetSize()

        # Calculate sizes based on percentages
        panel_width = int(width * 0.2)   # 20% of the width
        panel_height = int(height * 0.2)  # 20% of the height

        # Set the size of the panel
        self.panel.SetSize(panel_width, panel_height)

        # Call the event handler
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size Percentage')
    app.MainLoop()
