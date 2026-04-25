
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Create a panel to hold items
        panel = wx.Panel(self)

        # Create a vertical box sizer
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Create controls and specify proportion for sizing (0 - proportionate size)
        button1 = wx.Button(panel, label='Button 1')
        button2 = wx.Button(panel, label='Button 2')

        vbox.Add(button1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(button2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Set the sizer to the panel
        panel.SetSizer(vbox)

        # Show the frame
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size Example')
    app.MainLoop()
