
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(800, 600))

        # Get the size of the frame to calculate percentages
        width, height = self.GetSize()

        # Define size as percentages
        percent_width = int(width * 0.2)  # 20% of the width
        percent_height = int(height * 0.2)  # 20% of the height

        # Create a panel with the calculated size
        panel = wx.Panel(self, size=(percent_width, percent_height))
        panel.SetBackgroundColour(wx.Colour(100, 100, 250))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
