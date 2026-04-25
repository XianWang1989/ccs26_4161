
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set the size in pixels based on desired percentage
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.Show()

    def on_resize(self, event):
        size = self.GetSize()
        width = size[0] // 100 * 20  # 20% of the current width
        height = size[1] // 100 * 20  # 20% of the current height
        self.SetSize((width, height))
        event.Skip()

if __name__ == '__main__':
    app = wx.App(False)
    frame = Example(None, title='Size')
    frame.SetSize((250, 200))  # Initial size
    app.MainLoop()
