
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        self.panel = wx.Panel(self)
        self.SetInitialSize()

        self.Show()

    def SetInitialSize(self):
        width, height = self.GetSize()

        # Convert desired percentages to pixel sizes
        panel_width = int(width * 0.2)  # 20% of the width
        panel_height = int(height * 0.2)  # 20% of the height

        # Create a child panel with calculated size
        child_panel = wx.Panel(self.panel, size=(panel_width, panel_height))
        child_panel.SetBackgroundColour(wx.Colour(255, 0, 0))  # Red background

        # Center the child panel
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(child_panel, 0, wx.CENTER)
        self.panel.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
