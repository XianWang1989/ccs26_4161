
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.panel = wx.Panel(self)

        self.Show()

    def on_resize(self, event):
        # Get the size of the window
        width, height = self.GetSize()

        # Calculate size based on percentages
        new_width = int(width * 0.2)  # 20%
        new_height = int(height * 0.2)  # 20%

        # Set the size of the panel or other widgets
        self.panel.SetSize((new_width, new_height))
        self.panel.SetBackgroundColour('light blue')
        self.Layout()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
