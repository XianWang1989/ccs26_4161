
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Call to get layout size percentage
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Show()

    def on_size(self, event):
        width, height = self.GetSize()
        # Calculate sizes in percentage
        new_width = int(width * 0.2)  # 20% of current width
        new_height = int(height * 0.2)  # 20% of current height
        self.SetSize(new_width, new_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
