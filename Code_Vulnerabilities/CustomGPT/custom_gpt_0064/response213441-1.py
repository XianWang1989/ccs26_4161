
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.Bind(wx.EVT_SIZE, self.on_resize)  # Bind resize event
        self.Show()

    def on_resize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate the desired size as 20% of the current size
        new_width = int(width * 0.2)
        new_height = int(height * 0.2)

        # Set the size of the frame (new size as 20% of the current size)
        self.SetSize((new_width, new_height))
        event.Skip()  # Allow the event to propagate

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
