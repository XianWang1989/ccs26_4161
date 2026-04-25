
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set a default size
        self.default_width = 800
        self.default_height = 600
        self.SetSize((self.calculate_size(self.default_width, 20), 
                       self.calculate_size(self.default_height, 20)))

        self.Show()

    def calculate_size(self, total_size, percentage):
        """Convert percentage to pixels based on total size."""
        return int((percentage / 100) * total_size)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size as Percentage')
    app.MainLoop()
