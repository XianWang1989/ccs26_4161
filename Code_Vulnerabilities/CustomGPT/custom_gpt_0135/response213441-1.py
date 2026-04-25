
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Create a panel to hold your controls
        panel = wx.Panel(self)

        # Set size to 20% of the parent size
        self.SetInitialSize(self.calculate_size(0.2, 0.2))

        self.Show()

    def calculate_size(self, width_pct, height_pct):
        # Get the size of the frame (parent window)
        width, height = self.GetSize()

        # Calculate size based on percentage
        new_width = int(width * width_pct)
        new_height = int(height * height_pct)

        return (new_width, new_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size Example')
    app.MainLoop()
