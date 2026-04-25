
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Set up a panel and add a control with size in percentage
        panel = wx.Panel(self)

        # Calculate the width and height as a percentage of the frame's size
        self.Bind(wx.EVT_SIZE, self.on_resize)

        # Show the frame
        self.Show()

    def on_resize(self, event):
        size = self.GetSize()
        width, height = size

        # Set dimensions as percentages
        percent_width = int(width * 0.2)  # 20% of width
        percent_height = int(height * 0.2)  # 20% of height

        # Create a button with a size of 20% width and height
        button = wx.Button(self, label="Click Me", size=(percent_width, percent_height))
        button.SetPosition((width * 0.4, height * 0.4))  # Centering the button

        # Layout
        self.Layout()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
