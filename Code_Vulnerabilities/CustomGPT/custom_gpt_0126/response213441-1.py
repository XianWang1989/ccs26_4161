
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Get the size of the frame
        self.Bind(wx.EVT_SIZE, self.on_size)

        self.Show()

    def on_size(self, event):
        # Get current size of the window
        width, height = self.GetSize()

        # Calculate size as percentages
        new_width = int(width * 0.2)  # 20% of current width
        new_height = int(height * 0.2)  # 20% of current height

        # Set the size of a control, for example, a panel
        panel = wx.Panel(self)
        panel.SetSize(new_width, new_height)
        panel.SetBackgroundColour("light blue")

        event.Skip()  # Ensure the event is processed

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percent')
    app.MainLoop()
