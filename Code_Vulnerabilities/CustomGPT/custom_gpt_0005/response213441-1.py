
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Get the size of the parent frame
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.SetMinSize((250, 200))  # Set minimum size

        self.Show()

    def on_size(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate size in terms of percentages
        percent_width = int(width * 0.20)  # 20% of the width
        percent_height = int(height * 0.20)  # 20% of the height

        # Set new size based on percentage
        self.SetSize((percent_width, percent_height))

        event.Skip()  # Allow the event to propagate

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
