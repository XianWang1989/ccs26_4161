
# -*- coding: utf-8 -*-

import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        self.Bind(wx.EVT_SIZE, self.OnResize)
        self.panel = wx.Panel(self)

        self.Show()

    def OnResize(self, event):
        width, height = self.GetClientSize()

        # Calculate percentage dimensions
        panel_width = int(width * 0.2)  # 20%
        panel_height = int(height * 0.2)  # 20%

        # Set panel size
        self.panel.SetSize(panel_width, panel_height)
        self.panel.SetPosition((width - panel_width, height - panel_height))  # Bottom-right corner

        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size Percentage Example')
    app.MainLoop()
