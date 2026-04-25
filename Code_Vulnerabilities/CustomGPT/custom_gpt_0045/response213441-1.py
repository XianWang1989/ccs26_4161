
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Create a panel
        panel = wx.Panel(self)

        # Create a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Get the size of the parent frame
        width, height = self.GetSize()

        # Set size based on percentage
        percentage_width = int(width * 0.2)  # 20% of width
        percentage_height = int(height * 0.2)  # 20% of height

        # Create a button with specified percentage size
        btn = wx.Button(panel, label="Button", size=(percentage_width, percentage_height))

        # Add the button to the sizer
        sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)

        # Set the sizer for the panel
        panel.SetSizer(sizer)

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
