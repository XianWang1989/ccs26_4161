
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Calculate size based on percentages
        self.percent_width = 0.20  # 20%
        self.percent_height = 0.20  # 20%

        # Set the size after the frame is shown to ensure dimensions are available
        self.Bind(wx.EVT_SIZE, self.on_size)

        self.Show()

    def on_size(self, event):
        # Get the current size of the window
        width, height = self.GetSize()

        # Calculate new size based on percentage
        new_width = int(width * self.percent_width)
        new_height = int(height * self.percent_height)

        # Set the new size
        self.SetSize(new_width, new_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percentages')
    app.MainLoop()
