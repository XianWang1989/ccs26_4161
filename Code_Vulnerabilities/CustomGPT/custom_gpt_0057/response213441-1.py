
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(600, 400))
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.panel = wx.Panel(self)

        self.Show()

    def on_resize(self, event):
        width, height = selfGetSize()  # Get the current size of the window
        new_width = width * 0.2  # 20% of the width
        new_height = height * 0.2  # 20% of the height

        self.panel.SetSize(new_width, new_height)  # Set size in pixels
        self.panel.SetPosition((width * 0.4, height * 0.4))  # Center it

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percentage')
    app.MainLoop()
