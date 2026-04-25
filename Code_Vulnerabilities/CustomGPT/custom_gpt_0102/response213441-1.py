
# -*- coding: utf-8 -*-
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(300, 250))

        # Binding event to resize the frame
        self.Bind(wx.EVT_SIZE, self.on_resize)

        # Setting an initial layout size
        self.panel = wx.Panel(self)
        self.SetSizePercentage(20, 20)

        self.Show()

    def SetSizePercentage(self, width_percent, height_percent):
        # Get the current size of the frame
        frame_size = self.GetSize()

        # Calculate new size based on percentages
        new_width = int(frame_size[0] * (width_percent / 100))
        new_height = int(frame_size[1] * (height_percent / 100))

        # Set the new size
        self.panel.SetSize((new_width, new_height))
        self.panel.SetPosition((frame_size[0] - new_width, frame_size[1] - new_height))

    def on_resize(self, event):
        # Adjust panel size when the frame is resized
        self.SetSizePercentage(20, 20)
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percentage')
    app.MainLoop()
