
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.SetInitialSize(wx.Size(400, 300))  # Set an initial size for the frame

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("light blue")

        self.Show()

    def on_resize(self, event):
        self.panel.SetSize(self.GetClientSize().width * 0.2, self.GetClientSize().height * 0.2)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in Percentages')
    app.MainLoop()
