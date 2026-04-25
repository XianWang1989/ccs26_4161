
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set the dimensions of the frame
        self.SetSize((250, 200))
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))  # White background

        self.Show()

    def on_resize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate new sizes based on percentage
        panel_width = int(width * 0.2)  # 20% of the width
        panel_height = int(height * 0.2)  # 20% of the height

        # Set the new size for the panel
        self.panel.SetSize((panel_width, panel_height))
        self.panel.Centre()  # Center the panel within the frame

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
