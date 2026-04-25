
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.Bind(wx.EVT_SIZE, self.OnResize)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("light blue")

        self.Show()

    def OnResize(self, event):
        # Get new size of the frame
        width, height = self.GetSize()

        # Calculate new size for the panel in terms of percentage
        panel_width = int(width * 0.2)  # 20% of width
        panel_height = int(height * 0.2)  # 20% of height

        # Set the new size
        self.panel.SetSize(panel_width, panel_height)
        self.panel.Center()  # Centering the panel in the frame

        event.Skip()  # Ensure the event is processed properly

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
