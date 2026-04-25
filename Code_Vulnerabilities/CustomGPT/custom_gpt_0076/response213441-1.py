
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.Show()

    def on_resize(self, event):
        width, height = self.GetSize()
        # Calculating sizes as percentage of window size
        new_width = int(width * 0.2)  # 20%
        new_height = int(height * 0.2)  # 20%

        # Update the panel size
        self.panel.SetSize(new_width, new_height)
        self.panel.Centre()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percentage')
    app.MainLoop()
