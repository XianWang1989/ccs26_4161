
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(600, 400))

        # Calculate size based on percentage
        self.SetSize(self.calculate_size_from_percentage(20, 20))

        self.Show()

    def calculate_size_from_percentage(self, width_percentage, height_percentage):
        # Get the size of the frame
        frame_width, frame_height = self.GetSize()

        # Calculate the width and height in pixels
        new_width = int(frame_width * (width_percentage / 100))
        new_height = int(frame_height * (height_percentage / 100))

        return (new_width, new_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
