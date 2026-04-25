
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Create a panel
        self.panel = wx.Panel(self)

        # Create a button with initial size
        self.button = wx.Button(self.panel, label="Resize Me")
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)

        # Sizer to manage layout
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.button, 0, wx.ALL | wx.EXPAND, 10)

        self.panel.SetSizer(self.sizer)
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.Show()

    def on_resize(self, event):
        # Get new size of the frame
        width, height = self.GetSize()

        # Calculate size in pixels
        button_width = int(width * 0.2)  # 20% of the frame width
        button_height = int(height * 0.2)  # 20% of the frame height

        # Set the size of the button
        self.button.SetSize(button_width, button_height)

        # Ensure the layout updates
        self.panel.Layout()

    def on_button_click(self, event):
        wx.MessageBox('This button resizes based on window size!', 'Info', wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App(False)
    Example(None, title='Resize Example')
    app.MainLoop()
