
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Bind the size event to update sizes on resize
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a button and add it to the sizer
        self.button = wx.Button(self.panel, label="Button")
        self.sizer.Add(self.button, 0, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizer(self.sizer)
        self.Layout()

        self.Show()

    def on_resize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate size based on percentages
        button_width = int(width * 0.2)  # 20% of the width
        button_height = int(height * 0.2)  # 20% of the height

        self.button.SetSize(button_width, button_height)
        self.Layout()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
