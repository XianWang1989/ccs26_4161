
# -*- coding: utf-8 -*-
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Bind the size event to handle size changes
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.panel = wx.Panel(self)

        self.Show()

    def OnSize(self, event):
        # Get the size of the frame
        width, height = self.GetSize()

        # Calculate 20% of the width and height
        panel_width = int(width * 0.2)  # 20% width
        panel_height = int(height * 0.2)  # 20% height

        # Set the panel size
        self.panel.SetSize(panel_width, panel_height)
        self.panel.SetBackgroundColour(wx.Colour(100, 150, 200))

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
