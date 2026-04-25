
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Bind the size event to adjust controls when the window is resized
        self.Bind(wx.EVT_SIZE, self.on_size)

        # Initially create the controls
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label="Button", pos=(0, 0))

        self.on_size()  # Set initial sizes

        self.Show()

    def on_size(self, event=None):
        # Get the size of the frame
        width, height = self.GetSize()

        # Calculate sizes based on percentages
        button_width = int(width * 0.2)  # 20% of the width
        button_height = int(height * 0.2)  # 20% of the height

        # Resize the button
        self.button.SetSize(button_width, button_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
