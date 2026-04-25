
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Bind the event to calculate and resize when the frame is created
        self.Bind(wx.EVT_SIZE, self.onResize)

        self.Show()

    def onResize(self, event):
        # Get the size of the frame
        width, height = self.GetSize()

        # Calculate sizes based on percentages
        new_width = int(width * 0.2)  # 20% of the frame width
        new_height = int(height * 0.2)  # 20% of the frame height

        # Create a panel with size in percentage of the frame
        panel = wx.Panel(self, size=(new_width, new_height))
        panel.SetBackgroundColour(wx.Colour(200, 200, 200))  # Gray background

        # Refresh the layout
        self.Layout()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in Percentage')
    app.MainLoop()
