
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(400, 300))

        # Bind the event to resize the frame
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Add a button with size in percentage
        self.button = wx.Button(self.panel, label='Click Me')
        self.sizer.Add(self.button, 0, wx.ALL | wx.EXPAND, 10)

        self.panel.SetSizer(self.sizer)
        self.Show()

    def on_resize(self, event):
        # Get the new size of the frame
        width, height = self.GetSize()

        # Calculate size in pixels based on percentage
        button_width = int(width * 0.2)  # 20% of width
        button_height = int(height * 0.2)  # 20% of height

        # Set button size
        self.button.SetSize(button_width, button_height)

        event.Skip()  # Allow further event processing

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Layout Size in Percent')
    app.MainLoop()
