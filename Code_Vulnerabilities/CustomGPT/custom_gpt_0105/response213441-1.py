
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Bind the size event to a method
        self.Bind(wx.EVT_SIZE, self.on_resize)

        # Set the initial size (just for demonstration)
        self.SetSize((400, 300))
        self.Show()

    def on_resize(self, event):
        # Get the dimensions of the parent window
        width, height = self.GetSize()

        # Calculate width and height as 20% of the parent window's dimensions
        new_width = int(width * 0.2)
        new_height = int(height * 0.2)

        # Set the size using the calculated values
        self.SetSize((new_width, new_height))
        event.Skip()  # Allow the event to be processed further

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in Percentage')
    app.MainLoop()
