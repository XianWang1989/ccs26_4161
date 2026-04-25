
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Bind to the size event to adjust the layout
        self.Bind(wx.EVT_SIZE, self.onResize)
        self.panel = wx.Panel(self)

        self.Show()

    def onResize(self, event):
        w, h = self.GetSize()  # Get current frame size
        percent_width = int(w * 0.2)  # 20% width
        percent_height = int(h * 0.2)  # 20% height
        self.panel.SetSize((percent_width, percent_height))  # Set panel size
        self.Layout()  # Update the layout

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
