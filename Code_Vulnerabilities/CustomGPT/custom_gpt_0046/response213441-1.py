
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Calculate size in pixels based on percentage
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.Show()

    def on_resize(self, event):
        width, height = self.GetSize()

        # Set size in percentages
        size_percentage = (0.2 * width, 0.2 * height)  # 20% of width and height
        self.SetSize(size_percentage)

        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
