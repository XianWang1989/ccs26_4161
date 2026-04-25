
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))
        self.Bind(wx.EVT_SIZE, self.OnResize)

        # Create a panel to hold the widgets
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label="Click Me")

        # Initially set the size based on a percentage
        self.UpdateSize()

        self.Show()

    def UpdateSize(self):
        width, height = self.GetSize()

        # Convert percentages to pixels
        button_width = int(width * 0.2)  # 20%
        button_height = int(height * 0.2)  # 20%

        self.button.SetSize(button_width, button_height)
        self.button.Centre()

    def OnResize(self, event):
        self.UpdateSize()
        event.Skip()  # Allow the event to be processed

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in %')
    app.MainLoop()
