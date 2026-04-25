
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Bind the 'Size' event to update size based on percentage
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.panel = wx.Panel(self)
        self.Show()

    def OnSize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate the new size using percentages
        new_width = int(width * 0.2)  # 20% of the width
        new_height = int(height * 0.2)  # 20% of the height

        # Resize the panel
        self.panel.SetSize(new_width, new_height)
        self.panel.SetBackgroundColour('lightblue')  # Optional: Change background color
        self.Layout()  # Refresh layout

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
