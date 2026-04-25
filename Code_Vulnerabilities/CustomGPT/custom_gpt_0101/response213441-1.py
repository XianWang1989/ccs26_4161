
# -*- coding: utf-8 -*-

# size.py

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.SetInitialSize(wx.Size(self.calculate_size(20), self.calculate_size(20)))
        self.Show()

    def calculate_size(self, percentage):
        screen_width, screen_height = wx.GetDisplaySize()
        return int((percentage / 100) * screen_width)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
