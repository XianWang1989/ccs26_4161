
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(600, 400))

        # Bind the event to adjust size after the frame is shown
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Centre()

    def on_size(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate 20% of the frame dimensions
        new_width = int(width * 0.2)
        new_height = int(height * 0.2)

        # Create a panel with 20% size
        if not hasattr(self, 'panel'):
            self.panel = wx.Panel(self, size=(new_width, new_height))
            self.panel.SetBackgroundColour(wx.Colour(100, 150, 200))
        else:
            self.panel.SetSize((new_width, new_height))

        self.Layout()  # Layout the panel correctly

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
