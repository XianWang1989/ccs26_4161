
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Bind(wx.EVT_SIZE, self.OnResize)

        # Initial layout call
        self.LayoutComponents()

        self.Show()

    def OnResize(self, event):
        self.LayoutComponents()
        event.Skip()

    def LayoutComponents(self):
        width, height = self.GetSize()

        # Calculating sizes based on percentages
        button_width = int(width * 0.20)  # 20% of the width
        button_height = int(height * 0.20)  # 20% of the height

        button = wx.Button(self, label='Click Me', size=(button_width, button_height))
        button.Centre()  # Centre the button

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
