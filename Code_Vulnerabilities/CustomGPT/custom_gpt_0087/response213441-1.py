
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Set up the panel
        self.panel = wx.Panel(self)
        self.layout()

        self.Show()

    def layout(self):
        # Get current size of the frame
        width, height = self.GetSize()

        # Calculate size in pixels based on percentages
        width_percent = int(width * 0.20)  # 20% of width
        height_percent = int(height * 0.20)  # 20% of height

        # Create a button with size in percentage
        button = wx.Button(self.panel, label="Button", size=(width_percent, height_percent))
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        # Center the button
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button, 0, wx.ALIGN_CENTER | wx.TOP, 20)
        self.panel.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
