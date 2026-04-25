
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Bind the resize event to handle dynamic resizing
        self.Bind(wx.EVT_SIZE, self.on_resize)

        # Initial layout
        self.on_resize(None)
        self.Show()

    def on_resize(self, event):
        # Get the size of the current frame
        width, height = self.GetSize()

        # Define the percentage values
        percent_width = 0.20  # 20%
        percent_height = 0.20  # 20%

        # Calculate the new size based on the percentages
        new_width = int(width * percent_width)
        new_height = int(height * percent_height)

        # Resize frame to the new size
        self.SetSize(new_width, new_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in Percentage')
    app.MainLoop()
