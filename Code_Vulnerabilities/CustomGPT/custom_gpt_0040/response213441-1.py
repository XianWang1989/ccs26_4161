
# -*- coding: utf-8 -*-

import wx

class PercentFrame(wx.Frame):
    def __init__(self, parent, title):
        super(PercentFrame, self).__init__(parent, title=title, size=(800, 600))

        # Set size in percentage
        self.SetPercentageSize(20, 20)

        self.Show()

    def SetPercentageSize(self, width_percent, height_percent):
        width, height = self.GetSize()
        new_width = int((width * width_percent) / 100)
        new_height = int((height * height_percent) / 100)
        self.SetSize(new_width, new_height)

if __name__ == '__main__':
    app = wx.App()
    PercentFrame(None, title='Size in Percentage')
    app.MainLoop()
