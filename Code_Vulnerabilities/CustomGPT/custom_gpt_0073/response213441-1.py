
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Get the size of the frame
        width, height = self.GetSize()

        # Calculate sizes based on percentages
        width_percentage = int(width * 0.2)   # 20% width
        height_percentage = int(height * 0.2) # 20% height

        # Create a panel with the calculated size
        panel = wx.Panel(self, size=(width_percentage, height_percentage))
        panel.SetBackgroundColour(wx.Colour(0, 255, 0))  # Green panel for visibility

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
