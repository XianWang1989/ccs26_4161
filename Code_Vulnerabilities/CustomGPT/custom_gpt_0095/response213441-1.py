
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Bind the event to set the size after the window is shown
        self.Bind(wx.EVT_SHOWN, self.on_show)

        self.Show()

    def on_show(self, event):
        # Get the size of the parent window
        width, height = self.GetParent().GetSize()

        # Calculate sizes based on percentage (20% of each dimension)
        new_width = int(width * 0.2)
        new_height = int(height * 0.2)

        # Set the new size
        self.SetSize(new_width, new_height)

if __name__ == '__main__':
    app = wx.App()
    # Create a parent frame to get the size
    parent_frame = wx.Frame(None, title='Parent Frame', size=(800, 600))
    parent_frame.Show()

    Example(parent_frame, title='Size in %')
    app.MainLoop()
