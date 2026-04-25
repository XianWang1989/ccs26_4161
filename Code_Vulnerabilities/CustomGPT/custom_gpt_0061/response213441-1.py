
# -*- coding: utf-8 -*-
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(400, 300))

        # Start layout with a specific size, calculating based on a percentage
        self.panel = wx.Panel(self)

        # Get the size of the frame
        frame_width, frame_height = self.GetSize()

        # Calculate the percentage sizes
        width = int(frame_width * 0.2)  # 20% of the width
        height = int(frame_height * 0.2)  # 20% of the height

        # Set the size of the panel using calculated pixel values
        self.panel.SetSize((width, height))
        self.panel.SetBackgroundColour(wx.Colour(255, 0, 0))  # Red background for visibility

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
