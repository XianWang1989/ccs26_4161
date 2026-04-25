
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Call Layout after the Frame is shown to get actual size
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.Show()

    def on_resize(self, event):
        # Get current size of the Frame
        width, height = self.GetSize()

        # Calculate new size as a percentage
        new_width = int(width * 0.2)  # 20%
        new_height = int(height * 0.2)  # 20%

        # Set size of a panel, can change to your desired widget
        panel = wx.Panel(self)
        panel.SetSize((new_width, new_height))
        panel.Layout()  # Ensure the panel is laid out correctly

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percentage')
    app.MainLoop()
