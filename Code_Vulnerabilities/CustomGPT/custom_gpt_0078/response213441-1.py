
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Bind the resize event to update the size based on percentages
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.SetSize((500, 400))  # Set an initial size for the frame

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))  # Optional: Set panel background color

        self.Show()

    def on_resize(self, event):
        width, height = self.GetSize()

        # Calculate size based on percentage
        panel_width = int(width * 0.2)  # 20% of the width
        panel_height = int(height * 0.2)  # 20% of the height

        self.panel.SetSize(panel_width, panel_height)
        self.panel.Centre()  # Center the panel in the frame

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
