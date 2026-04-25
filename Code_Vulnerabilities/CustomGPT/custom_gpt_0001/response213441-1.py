
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title) 

        # Set initial size in pixels
        self.SetInitialSize((250, 200))

        # Bind the size event to adjust the size in percentages
        self.Bind(wx.EVT_SIZE, self.on_size)

        self.Show()

    def on_size(self, event):
        frame_size = self.GetSize()

        # Calculate sizes in terms of percentages
        width_percentage = int(frame_size[0] * 0.20)  # 20% of the frame's width
        height_percentage = int(frame_size[1] * 0.20)  # 20% of the frame's height

        self.SetSize((width_percentage, height_percentage))
        event.Skip()  # keep processing the size event

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in Percentage')
    app.MainLoop()
