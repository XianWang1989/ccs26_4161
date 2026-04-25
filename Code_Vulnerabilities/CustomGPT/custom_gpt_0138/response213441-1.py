
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Bind the size event
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.panel = wx.Panel(self)

        self.Show()

    def on_size(self, event):
        # Get current size of the frame
        width, height = self.GetSize()

        # Calculate sizes as percentages
        percentage_width = int(0.2 * width)  # 20% of the width
        percentage_height = int(0.2 * height)  # 20% of the height

        # Set the panel size
        self.panel.SetSize((percentage_width, percentage_height))
        self.panel.SetBackgroundColour('light blue')  # Optional: set background color

        event.Skip()  # Allow other handlers to process the event

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
