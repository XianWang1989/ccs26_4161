
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Bind the size event to the handler
        self.Bind(wx.EVT_SIZE, self.OnResize)

        # Store initial size
        self.initial_size = (250, 200)
        self.SetSize(self.initial_size)

        self.Show()

    def OnResize(self, event):
        # Get the size of the parent window
        width, height = self.GetSize()

        # Calculate new size as 20% of the current size
        new_width = int(width * 0.2)
        new_height = int(height * 0.2)

        # Set the new size
        self.SetSize((new_width, new_height))

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
