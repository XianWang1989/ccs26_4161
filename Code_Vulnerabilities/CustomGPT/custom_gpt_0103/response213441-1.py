
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Set the frame to a specific size and then adjust content size using percentages
        self.panel = wx.Panel(self)
        self.SetSize(WxUtil.get_percent_size(self, 20, 20))  # Using 20% for width and height

        self.Show()

class WxUtil:
    @staticmethod
    def get_percent_size(frame, width_percent, height_percent):
        width = frame.GetSize()[0] * (width_percent / 100)
        height = frame.GetSize()[1] * (height_percent / 100)
        return int(width), int(height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
