
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Create a panel
        panel = wx.Panel(self)

        # Set up sizer to manage layout
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Convert percentage to pixel size based on current size
        width, height = self.GetSize()
        button_size = (int(0.2 * width), int(0.2 * height))  # 20% of width and height

        # Create a button with size based on percentage
        button = wx.Button(panel, label="Button", size=button_size)
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(sizer)

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
