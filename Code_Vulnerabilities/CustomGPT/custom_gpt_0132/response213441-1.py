
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get parent size
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.SetInitialSize((250, 200))  # Initial frame size

    def on_size(self, event):
        self.Layout()  # Refresh layout on resize

        # Get current size of the frame
        width, height = self.GetSize()

        # Calculate size based on percentage (20%)
        new_width = int(width * 0.2)
        new_height = int(height * 0.2)

        # Create a new panel with size in pixels
        panel = wx.Panel(self, size=(new_width, new_height))
        panel.SetBackgroundColour(wx.GREEN)  # Just to visualize the panel
        panel.Layout()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
