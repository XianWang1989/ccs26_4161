
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Bind the size event to our method
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("light blue")

        self.Show()

    def on_resize(self, event):
        # Get the new size of the frame
        width, height = self.GetSize()

        # Calculate sizes based on percentages
        new_width = int(width * 0.2)  # 20% of width
        new_height = int(height * 0.2)  # 20% of height

        # Set the size of the panel
        self.panel.SetSize(new_width, new_height)
        self.panel.Center()  # Center the panel

        event.Skip()  # Allow further processing of the event

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
