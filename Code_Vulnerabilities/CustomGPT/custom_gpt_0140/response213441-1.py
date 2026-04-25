
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(800, 600))

        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a button with size set to 20% width and height
        btn_width = int(self.GetSize()[0] * 0.2)  # 20% of frame width
        btn_height = int(self.GetSize()[1] * 0.2)  # 20% of frame height
        button = wx.Button(self.panel, label="Click Me", size=(btn_width, btn_height))

        self.sizer.Add(button, 0, wx.CENTER | wx.ALL, 10)
        self.panel.SetSizer(self.sizer)

        self.Bind(wx.EVT_BUTTON, self.on_click, button)
        self.Show()

    def on_click(self, event):
        wx.MessageBox("Button clicked!", "Info", wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size Example')
    app.MainLoop()
