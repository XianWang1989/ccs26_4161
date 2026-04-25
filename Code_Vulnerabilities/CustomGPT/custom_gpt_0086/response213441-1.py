
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Set the size based on percentages
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.Show()

    def on_resize(self, event):
        # Get the size of the frame
        width, height = self.GetSize()

        # Calculate the desired size as a percentage
        new_width = int(width * 0.2)  # 20% of the width
        new_height = int(height * 0.2)  # 20% of the height

        # Create a panel with the calculated size
        panel = wx.Panel(self, size=(new_width, new_height))
        panel.SetBackgroundColour(wx.Colour(255, 255, 255))  # Set a background color

        # Layout the panel
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(panel, 0, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(layout)

        # Refresh the layout
        self.Layout()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
