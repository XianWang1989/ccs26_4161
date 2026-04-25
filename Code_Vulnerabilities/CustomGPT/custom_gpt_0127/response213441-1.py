
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Bind the resize event to calculate sizes dynamically
        self.Bind(wx.EVT_SIZE, self.on_resize)

        # Create a panel to demonstrate size calculation
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(200, 200, 250))  # Light blue color

        self.Show()

    def on_resize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Convert percentage to pixel size
        panel_width = int(width * 0.20)  # 20% of the frame width
        panel_height = int(height * 0.20)  # 20% of the frame height

        # Set the panel size
        self.panel.SetSize(panel_width, panel_height)
        self.panel.Centre()  # Center the panel in the frame

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Percentage Size Example')
    app.MainLoop()
