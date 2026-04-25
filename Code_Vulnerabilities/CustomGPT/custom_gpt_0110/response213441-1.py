
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.panel = wx.Panel(self)

        self.Show()

    def on_resize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate the size as 20% of the width and height
        new_width = int(width * 0.2)
        new_height = int(height * 0.2)

        # Resize the panel using calculated pixel sizes
        self.panel.SetSize(new_width, new_height)
        self.panel.SetBackgroundColour(wx.Colour(255, 0, 0))  # Red background for visibility

if __name__ == '__main__':
    app = wx.App(False)
    Example(None, title='Size')
    app.MainLoop()
