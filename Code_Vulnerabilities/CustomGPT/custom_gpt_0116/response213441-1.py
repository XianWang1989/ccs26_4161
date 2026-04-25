
# -*- coding: utf-8 -*-
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set the initial size
        self.SetSize(self.get_size_from_percentage(20, 20))

        self.Show()

    def get_size_from_percentage(self, width_percentage, height_percentage):
        # Get the screen size
        screen_size = wx.GetDisplaySize()
        # Calculate the size based on percentage
        width = int(screen_size[0] * (width_percentage / 100))
        height = int(screen_size[1] * (height_percentage / 100))
        return (width, height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percentage')
    app.MainLoop()
