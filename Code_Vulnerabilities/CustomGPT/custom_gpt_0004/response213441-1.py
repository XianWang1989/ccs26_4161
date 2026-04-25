
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Call to adjust size based on percentage
        self.SetSize(self.calculate_size(20, 20))  # 20% width and height

        self.Show()

    def calculate_size(self, width_percent, height_percent):
        screen_size = wx.GetDisplaySize()
        new_width = int(screen_size[0] * (width_percent / 100))
        new_height = int(screen_size[1] * (height_percent / 100))
        return (new_width, new_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
