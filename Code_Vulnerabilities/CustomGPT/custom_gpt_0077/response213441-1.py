
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Create a box sizer
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a button and add it to the sizer with proportion
        button = wx.Button(self, label='Button 1')
        sizer.Add(button, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Another button
        button2 = wx.Button(self, label='Button 2')
        sizer.Add(button2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Set the sizer for the frame
        self.SetSizer(sizer)

        # Show the frame
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
