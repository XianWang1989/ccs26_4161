
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.panel = wx.Panel(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Show()

    def OnSize(self, event):
        # Force a redraw when the frame is resized
        self.panel.Refresh()

    def OnPaint(self, event):
        dc = wx.PaintDC(self.panel)
        width, height = self.panel.GetSize()

        # Calculate sizes as percentages
        box_width = int(width * 0.2)  # 20% of the panel width
        box_height = int(height * 0.2)  # 20% of the panel height

        # Draw a rectangle based on calculated sizes
        dc.SetBrush(wx.Brush(wx.Colour(255, 0, 0)))
        dc.DrawRectangle(0, 0, box_width, box_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
