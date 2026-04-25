
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.panel = wx.Panel(self)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.Show()

    def on_resize(self, event):
        width, height = self.GetSize()

        # Calculate sizes based on percentages
        size_percentage = (0.2, 0.2)  # 20% width and height
        new_width = int(width * size_percentage[0])
        new_height = int(height * size_percentage[1])

        # Example of setting a new size (you can use the new sizes as needed)
        self.panel.SetSize(new_width, new_height)
        self.panel.SetPosition((width // 2 - new_width // 2, height // 2 - new_height // 2))

        self.panel.Refresh()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
