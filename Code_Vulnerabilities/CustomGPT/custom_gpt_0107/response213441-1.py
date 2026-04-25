
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(600, 400))

        # Get the current size of the window
        self.Bind(wx.EVT_SIZE, self.OnResize)
        self.Show()

    def OnResize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate size based on percentage
        new_width = int(width * 0.2)  # 20% width
        new_height = int(height * 0.2)  # 20% height

        # Set the size of the frame (or any other widget)
        self.SetSize(new_width, new_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
