
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Allow the frame to be resized
        self.Bind(wx.EVT_SIZE, self.on_resize)

        # Initial size calculated in pixels
        self.size_in_percent = (0.2, 0.2)  # 20% of size
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('lightblue')

        self.Show()

    def on_resize(self, event):
        # Get the new size of the frame
        width, height = self.GetSize()

        # Calculate the new size based on the percentage
        new_width = int(width * self.size_in_percent[0])
        new_height = int(height * self.size_in_percent[1])

        # Set the new size for the panel
        self.panel.SetSize(new_width, new_height)
        self.panel.Centre()  # Center the panel
        event.Skip()  # Allow the default processing of the event

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
