
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        panel = wx.Panel(self)
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.size_percent = (0.2, 0.2)  # 20% width and height

        self.Show()

    def on_resize(self, event):
        # Get current size of the frame
        width, height = self.GetSize()

        # Calculate new size based on percentage
        new_width = int(width * self.size_percent[0])
        new_height = int(height * self.size_percent[1])

        # Create a new child window with the calculated size
        self.panel = wx.Panel(self, size=(new_width, new_height))
        self.panel.SetBackgroundColour(wx.Colour(255, 0, 0))  # Optional: Set background color

        self.Layout()  # Adjust layout

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
