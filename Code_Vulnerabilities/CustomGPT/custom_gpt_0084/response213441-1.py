
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Bind the EVT_SIZE event to adjust the size of controls when the frame is resized
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('lightblue')

        # You can create a child control, for example, a button
        self.button = wx.Button(self.panel, label='Click Me')

        # Set the initial size
        self.update_size()

        self.Show()

    def on_resize(self, event):
        self.update_size()
        event.Skip()  # Call the base class event handler

    def update_size(self):
        width, height = self.GetSize()
        percentage_width = int(width * 0.2)  # 20% of the frame width
        percentage_height = int(height * 0.2)  # 20% of the frame height

        self.button.SetSize(percentage_width, percentage_height)  # Set the button size
        self.button.Center()  # Center the button in the panel

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
