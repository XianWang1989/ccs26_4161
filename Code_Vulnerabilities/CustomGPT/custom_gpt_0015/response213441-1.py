
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the size of the screen
        screen_width, screen_height = wx.GetScreenSize()

        # Calculate size as a percentage of the screen dimensions
        width = int(screen_width * 0.2)  # 20% of screen width
        height = int(screen_height * 0.2)  # 20% of screen height

        self.SetSize((width, height))  # Set the size of the frame
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
