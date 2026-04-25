
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.Show()

    def on_resize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Convert 20% of the width and height to pixels
        percent_width = int(width * 0.20)
        percent_height = int(height * 0.20)

        # Set a child panel size based on the calculated pixel values
        child_panel = wx.Panel(self)
        child_panel.SetSize((percent_width, percent_height))
        child_panel.SetBackgroundColour(wx.Colour(255, 0, 0))  # Red for visibility

        self.Layout()  # Update the layout

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in Percent')
    app.MainLoop()
