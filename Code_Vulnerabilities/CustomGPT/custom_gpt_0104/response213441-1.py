
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Create a panel
        panel = wx.Panel(self)

        # Set the window size based on the percentage of the frame size
        frame_width, frame_height = self.GetSize()
        button_size = (int(frame_width * 0.2), int(frame_height * 0.2))  # 20% of width and height

        # Create a button with the calculated size
        button = wx.Button(panel, label="Click Me", size=button_size)

        # Center the button in the panel
        button.Center()

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percentage')
    app.MainLoop()
