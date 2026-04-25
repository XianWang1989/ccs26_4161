
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Bind the size event to adjust child sizes when the frame is resized
        self.Bind(wx.EVT_SIZE, self.on_size)

        # Create a panel with a specific size percentage of the frame
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('lightblue')

        self.Show()

    def on_size(self, event):
        # Get the size of the frame
        width, height = self.GetSize()

        # Set the size of the panel as a percentage of the frame size
        panel_width = int(width * 0.2)  # 20% of frame width
        panel_height = int(height * 0.2)  # 20% of frame height

        self.panel.SetSize(panel_width, panel_height)
        self.panel.Center()  # Center the panel
        event.Skip()  # Allow the event to propagate

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
